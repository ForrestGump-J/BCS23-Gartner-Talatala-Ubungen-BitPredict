import ccxt
import streamlit as st
import networkx as nx
import pandas as pd
import numpy as np
import itertools
import matplotlib.pyplot as plt

exchange = ccxt.binanceus({
    "enableRateLimit": True,
})
COINS = ["BTC/USDT", "ETH/USDT", "XRP/USDT"]
MOVEMENT_THRESHOLD = 0.05  # 5%

def fetch_30day_data(symbol):
    data = exchange.fetch_ohlcv(symbol, timeframe="1d", limit=32)
    df = pd.DataFrame(data, columns=["time","open","high","low","close","vol"])
    return df


def classify_trend(df):
    df["pct_change"] = df["close"].pct_change()
    avg_change = df["pct_change"].sum()

    if avg_change >= MOVEMENT_THRESHOLD:
        return "BULL"
    elif avg_change <= -MOVEMENT_THRESHOLD:
        return "BEAR"
    else:
        return "STABLE"

def build_graph(price_dict):
    gr = nx.Graph()
    for coin in price_dict:
        gr.add_node(coin)
    
    coins = list(price_dict.keys())
    for i in range(len(coins)):
        for j in range(i+1, len(coins)):
            c1, c2 = coins[i], coins[j]
            correlation = np.corrcoef(price_dict[c1], price_dict[c2])[0][1]
            gr.add_edge(c1, c2, weight = round(correlation, 2))
    
    return gr

def show_graph(g):
    fig, ax = plt.subplots(figsize = (6, 4))
    posi = nx.spring_layout(g, seed=42)
    labels = nx.get_edge_attributes(g, "weight")

    nx.draw(g, posi, with_labels=True, node_color='cyan', node_size=1600, font_size=7, ax=ax)
    nx.draw_networkx_edge_labels(g, posi, edge_labels=labels, ax=ax)

    st.pyplot(fig)

def get_portfolio_combos():
    combinations = list(itertools.combinations(COINS, 2))
    return combinations

def main():
    st.title("BitPredict: Digital Currency Insight Program")
    st.write("Cryptocurrency Prediction Software Prototype\n\n")

    st.write("Fetching data...")

    option = st.selectbox("Which coin would you like to view the data?",COINS,index=None,placeholder="Select a cryptocuency.")

    st.write("Displaying data for:",option)

    if option:
        df = fetch_30day_data(option)
        df["time"] = pd.to_datetime(df["time"], unit="ms")
        df.set_index("time", inplace=True)

        df["pct_change"] = df["close"].pct_change()

        df_full = df.copy()
        df_display = df.iloc[1:].copy()
        trend = classify_trend(df_full)

        df_full = df.copy()
        df_display = df.iloc[1:].copy()

        st.subheader(f"30-Day Trend for {option}")
        st.write(f"**Trend Classification**: {trend}")

        st.line_chart(df_display["close"])
        st.dataframe(df_display)

    price_data = {}
    trend_classification = {}
    closing_only = {}

    for coin in COINS:
        df_all = fetch_30day_data(coin)
        price_data[coin] = df_all
        closing_only[coin] = df_all["close"].values
        trend_classification[coin] = classify_trend(df_all)

    bulls = {c for c in COINS if trend_classification[c] == "BULL"}
    bears = {c for c in COINS if trend_classification[c] == "BEAR"}
    stable = {c for c in COINS if trend_classification[c] == "STABLE"}

    st.subheader("Market Classifications")
    st.write("**BULLS**")
    st.dataframe(pd.DataFrame({"BULLS": list(bulls)}), hide_index=True)
    st.write("**BEARS**")
    st.dataframe(pd.DataFrame({"BEARS": list(bears)}), hide_index=True)
    st.write("**STABLE**")
    st.dataframe(pd.DataFrame({"STABLE": list(stable)}), hide_index=True)

    
    gra=build_graph(closing_only)
    show_graph(gra)

    st.subheader("Want to see possible portfolio combinations?")
    if st.button("Show", type="primary"):
        combos = get_portfolio_combos()
        for c in combos:
            st.write(c)


if __name__ == "__main__":
    main()