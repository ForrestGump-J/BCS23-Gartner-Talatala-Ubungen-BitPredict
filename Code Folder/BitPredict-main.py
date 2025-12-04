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
    avg_change = (1 + df["pct_change"]).prod() - 1


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
    combinations = []
    for r in range(1, len(COINS)+1):
        combinations.extend(itertools.combinations(COINS, r))
    return combinations

def score_combination(combo, trend_map):
    score_map = {"BULL": 1, "STABLE": 0, "BEAR": -1}
    return sum(score_map[trend_map[c]] for c in combo)

def main():
    st.title("BitPredict: Digital Currency Insight Program")
    st.write("Cryptocurrency Prediction Software Prototype\n\n")

    st.write("Fetching data...")

    option = st.selectbox("Which coin would you like to view the data?",COINS,index=None,placeholder="Select a cryptocurrency.")

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

        avg_change = round((((1 + df["pct_change"]).prod() - 1) * 100), 3)
        st.write(f"Total gain-loss percentage across 30 days: {avg_change}%")

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
        best_score = -999
        best_com = []
        for co in combos:
            sc = score_combination(co, trend_classification)
            st.write(f"{co} - Score: {sc}")

            if sc > best_score:
                best_score = sc
                best_com = [co]
            elif sc == best_score:
                best_com.append(co)
        
        st.subheader("Recommendation:")
        best_pretty = [", ".join(c) for c in best_com]

        bulls = {c for c, t in trend_classification.items() if t == "BULL"}

        if best_score < 0:
            st.error("Do not buy any coins. Market not safe.")
        elif best_score == 0 and len(bulls) == 0:
            st.warning(f"Best recommendation: {best_pretty}, but buy at your own risk. Market is unsafe.")
        else:
            st.success(f"Best recommendation: {best_pretty} (Score: {best_score})")
            
        
if __name__ == "__main__":
    main()