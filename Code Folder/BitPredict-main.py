import ccxt
import streamlit as st
import networkx as nx
import pandas as pd
import numpy as np
import itertools
import matplotlib.pyplot as plt
import pathlib


st.set_page_config(layout="centered")

def load_css(name):
    base = pathlib.Path(__file__).parent
    css_path = base / name
    with open(css_path, "r") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def image_path(name):
    baseim = pathlib.Path(__file__).parent
    return str(baseim / name)


load_css("style.css")

exchange = ccxt.binanceus({
    "enableRateLimit": True,
})
COINS = ["BTC/USDT", "ETH/USDT", "XRP/USDT"]

@st.cache_data(ttl=6300)
def fetch_data(symbol):
    data = exchange.fetch_ohlcv(symbol, timeframe="1d", limit=463)
    df = pd.DataFrame(data, columns=["Time","Open","High","Low","Close","Vol"])

    df["Time"] = pd.to_datetime(df["Time"], unit="ms")
    df.set_index("Time", inplace=True)

    df["Pct_change"] = df["Close"].pct_change()
    return df


def classify_ma_trend(df):
    df["MA50"] = df["Close"].rolling(50).mean()
    df["MA200"] = df["Close"].rolling(200).mean()

    price = df["Close"].iloc[-1]
    ma50 = df["MA50"].iloc[-1]
    ma200 = df["MA200"].iloc[-1]

    if pd.isna(ma200):
        return "STABLE"
    

    if ma50 > ma200:
        if price > ma50:
            return "BULL"
        else:
            return "CORRECTION"

    elif ma50 < ma200:
        if price > ma50:
            return "RALLY"
        else:
            return "BEAR" 

    
    return "STABLE"

def build_graph(price_dict):
    gr = nx.Graph()
    for coin in price_dict:
        gr.add_node(coin)
    
    coins = list(price_dict.keys())
    for i in range(len(coins)):
        for j in range(i+1, len(coins)):
            c1, c2 = coins[i], coins[j]

            min_len = min(len(price_dict[c1]), len(price_dict[c2]))
            s1 = price_dict[c1][-min_len:][-90:]
            s2 = price_dict[c2][-min_len:][-90:]
            
            correlation = np.corrcoef(s1, s2)[0][1]
            gr.add_edge(c1, c2, weight = round(correlation, 2))
    
    return gr

def show_graph(g):
    fig, ax = plt.subplots(figsize = (6, 4))
    posi = nx.spring_layout(g, seed=42)
    labels = nx.get_edge_attributes(g, "weight")

    nx.draw(g, posi, with_labels=True, node_color='lightsteelblue', node_size=1590, font_size=7.5, font_family="Courier New", ax=ax)
    nx.draw_networkx_edge_labels(g, posi, edge_labels=labels, ax=ax)

    st.pyplot(fig)

def get_portfolio_combos():
    combinations = []
    for r in range(1, len(COINS)+1):
        combinations.extend(itertools.combinations(COINS, r))
    return combinations

def score_combination(combo, trend_map):
    
    score_map = {"BULL": 2, "CORRECTION": 1, "STABLE": 0, "RALLY": -1, "BEAR": -2}
    return sum(score_map[trend_map[c]] for c in combo)

def main():

    col1, col2, col3= st.columns([1, 1, 1])
    with col2:
        st.image(image_path("BitPredict_nobg_cropped.png"))
    st.title("BitPredict: Digital Currency Insight Program")
    st.subheader("Cryptocurrency Prediction Software Prototype\n\n")

    with st.spinner("Fetching data from Binance..."):
        market_data = {}
        for coin in COINS:
            df_fetched = fetch_data(coin)
            if not df_fetched.empty:
                market_data[coin] = df_fetched
            else:
                st.error(f"Could not fetch data for {coin}")

    if not market_data:
        st.stop()
    option = st.selectbox("",COINS,index=None,placeholder="Select a cryptocurrency to analyze.")

    st.write("Displaying data for:",option)

    if option:
        df = market_data[option]
        ma_trend = classify_ma_trend(df)

        st.subheader(f"90-Day Trend for {option}")

        last_90 = df["Pct_change"].tail(90)
        roi_90 = ((1 + last_90).prod() - 1) * 100

        current_price = df["Close"].iloc[-1]

        st.metric(
            label="",
            value=f"{current_price:.2f} USDT",
            delta=f"{roi_90:.2f}%"
        )

        st.write(f"**Trend Classification**: {ma_trend}")

        chart_data = df[["Close", "MA50", "MA200"]].iloc[-90:]

        chart_data = chart_data.reset_index()

        chart_data = chart_data.rename(columns={"Time": "Date"})

        chart_data_long = chart_data.melt(
            id_vars=["Date"], 
            var_name="Line", 
            value_name="Value"
        )

        st.line_chart(
            chart_data_long,
            x="Date",
            y="Value",
            color="Line"
        )
        st.dataframe(df.drop(columns=["MA50", "MA200"]).iloc[-90:])

        # Gather all coins
        price_data = {}
        trend_classification = {}
        closing_only = {}

        for coin in COINS:
            df_all = fetch_data(coin)
            closing_only[coin] = df_all["Close"].values
            trend_classification[coin] = classify_ma_trend(df_all)

        bulls = {c for c in COINS if trend_classification[c] == "BULL"}
        bears = {c for c in COINS if trend_classification[c] == "BEAR"}
        stable = {c for c in COINS if trend_classification[c] == "STABLE"}
        rally = {c for c in COINS if trend_classification[c] == "RALLY"}
        correction = {c for c in COINS if trend_classification[c] == "CORRECTION"}

        st.subheader("Market Classifications")
        st.dataframe(pd.DataFrame({"BULL": list(bulls)}), hide_index=True)
        st.dataframe(pd.DataFrame({"BEAR": list(bears)}), hide_index=True)
        st.dataframe(pd.DataFrame({"STABLE": list(stable)}), hide_index=True)
        st.dataframe(pd.DataFrame({"RALLY": list(rally)}), hide_index=True)
        st.dataframe(pd.DataFrame({"CORRECTION": list(correction)}), hide_index=True)

        st.subheader("Correlation Graph for All Options")
        st.write("Each number on the line represents the weight of the connection between the two currencies or how similarly they move, 1 being the highest and -1 being the lowest.")
    
        gra=build_graph(closing_only)
        show_graph(gra)

        st.subheader("Want to see possible portfolio combinations?")
        col1, col2, col3, col4, col5, col6, col7, col8, col9= st.columns([1, 1, 1, 1, 1, 1, 1, 1, 1])
        with col5:
            show_combinations = st.button("Show", type="primary")

        if show_combinations:
            st.write("A scoring system is applied to each classification to suggest the best portfolio combination for you.  \n  \n**Bull stock = +2**  \n**Correction = +1**  \n**Stable stock = 0**  \n**Bear rally = -1**  \n**Bear stock = -2**")
            combos = get_portfolio_combos()
            best_score = -999
            best_com = []
            for co in combos:
                sc = score_combination(co, trend_classification)
                combo_name = " + ".join(co)
             
                if sc >= 3: 
                  
                    badge_color = "#00ff00"
                    border_style = "2px solid #00ff00"
                elif sc > 0:
                    badge_color = "#4cd073"
                    border_style = "none"
                elif sc == 0:
                    badge_color = "#888888"
                    border_style = "none"
                elif sc <= -3:
                    badge_color = "#ff0000"
                    border_style = "2px solid #ff0000"
                else:
                    badge_color = "#ff4b4b"
                    border_style = "none"
                    
                st.markdown(
                    f"""
                    <div class="combo-row">
                        <span class="combo-badge" style="color: {badge_color};">{combo_name}</span>
                        <span class="combo-score">Score: {sc}</span>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )

                if sc > best_score:
                    best_score = sc
                    best_com = [co]
                elif sc == best_score:
                    best_com.append(co)
        
            st.subheader("Recommendation:")
            best_to_buy = [", ".join(c) for c in best_com]
            final_string = " or ".join(best_to_buy)

            bulls = {c for c, t in trend_classification.items() if t == "BULL"}

            if best_score < 0:
                st.error("Market conditions unsafe. Do not invest until better conditions are met.")
    
            else:
                if len(bulls) == 0:
                    st.warning(f"Current best to buy: **{final_string}**. Caution: No assets are currently in a clear Bull trend. Market is unpredictable.")
                else:
                    st.success(f"Best combination for your portfolio: **{final_string}**")

if __name__ == "__main__":
    main()
