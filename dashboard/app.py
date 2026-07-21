import streamlit as st

from dashboard.database import (
    fetch_trade_summary,
    fetch_symbol_summary,
    fetch_exchange_summary,
    fetch_status_summary
)



st.set_page_config(
    page_title="Investment Analytics Platform",
    layout="wide"
)



st.title("📈 Investment Analytics Platform")


st.markdown(
    "Kafka + PostgreSQL powered investment analytics dashboard"
)



trade_df = fetch_trade_summary()

symbol_df = fetch_symbol_summary()

exchange_df = fetch_exchange_summary()

status_df = fetch_status_summary()



# =========================
# KPI SECTION
# =========================


st.header("Trading Overview")



if not trade_df.empty:

    row = trade_df.iloc[0]


    avg_trade = (
        row["total_trade_value"]
        /
        row["total_trades"]
    )


    c1,c2,c3,c4,c5 = st.columns(5)


    c1.metric(
        "Total Trades",
        f"{int(row['total_trades']):,}"
    )


    c2.metric(
        "Total Value",
        f"${row['total_trade_value']/1e9:.2f} B"
    )


    c3.metric(
        "BUY Trades",
        f"{int(row['buy_trades']):,}"
    )


    c4.metric(
        "SELL Trades",
        f"{int(row['sell_trades']):,}"
    )


    c5.metric(
        "Average Trade",
        f"${avg_trade:,.2f}"
    )



# =========================
# SYMBOL ANALYSIS
# =========================


st.header("Top Symbols by Trade Value")


st.bar_chart(
    symbol_df.set_index("symbol")
)



# =========================
# EXCHANGE
# =========================


st.header("Exchange Distribution")


st.bar_chart(
    exchange_df.set_index("exchange")
)



# =========================
# STATUS
# =========================


st.header("Trade Status")


st.bar_chart(
    status_df.set_index("status")
)



st.subheader("Status Details")


st.dataframe(
    status_df,
    use_container_width=True
)



# =========================
# TABLES
# =========================


st.header("Symbol Details")


st.dataframe(
    symbol_df,
    use_container_width=True
)



st.header("Exchange Details")


st.dataframe(
    exchange_df,
    use_container_width=True
)