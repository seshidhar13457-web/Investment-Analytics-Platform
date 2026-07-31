import streamlit as st
import plotly.express as px
from streamlit_autorefresh import st_autorefresh


from dashboard.database import (
    fetch_trade_summary,
    fetch_trade_history,
    fetch_symbol_summary,
    fetch_exchange_summary,
    fetch_status_summary,
    fetch_live_trades
)



# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Investment Analytics Platform",
    page_icon="📈",
    layout="wide"
)



# =====================================
# AUTO REFRESH
# =====================================

st_autorefresh(
    interval=5000,
    key="live_refresh"
)



# =====================================
# HEADER
# =====================================

st.title(
    "📈 Investment Analytics Platform"
)


st.markdown(
    """
    Real-Time Investment Analytics Dashboard

    **Kafka • PostgreSQL • Streamlit • Plotly**
    """
)



# =====================================
# LOAD DATA
# =====================================

trade_df = fetch_trade_summary()

history_df = fetch_trade_history()

symbol_df = fetch_symbol_summary()

exchange_df = fetch_exchange_summary()

status_df = fetch_status_summary()

live_df = fetch_live_trades()



# =====================================
# KPI SECTION
# =====================================

st.divider()

st.header(
    "📊 Trading Overview"
)


if not trade_df.empty:

    row = trade_df.iloc[0]


    total_trades = int(row["total_trades"])

    total_value = float(row["total_trade_value"])

    buy = int(row["buy_trades"])

    sell = int(row["sell_trades"])


    avg_trade = total_value / total_trades



    c1, c2, c3, c4, c5 = st.columns(5)


    c1.metric(
        "Total Trades",
        f"{total_trades:,}"
    )


    c2.metric(
        "Trade Value",
        f"${total_value:,.2f}"
    )


    c3.metric(
        "BUY Trades",
        f"{buy:,}"
    )


    c4.metric(
        "SELL Trades",
        f"{sell:,}"
    )


    c5.metric(
        "Avg Trade Size",
        f"${avg_trade:,.2f}"
    )



# =====================================
# HISTORY
# =====================================

st.divider()

st.header(
    "📈 Historical Trading Activity"
)


if not history_df.empty:


    fig = px.line(
        history_df,
        x="created_at",
        y="total_trades",
        markers=True,
        title="Trade Volume Over Time"
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )



# =====================================
# SYMBOL ANALYSIS
# =====================================

st.divider()

st.header(
    "📊 Top Symbols By Trade Value"
)


if not symbol_df.empty:


    fig = px.bar(
        symbol_df,
        x="symbol",
        y="trade_value",
        text_auto=".2s",
        title="Trade Value By Symbol"
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )



# =====================================
# EXCHANGE ANALYSIS
# =====================================

st.divider()

st.header(
    "🏦 Exchange Performance"
)


if not exchange_df.empty:


    fig = px.pie(
        exchange_df,
        names="exchange",
        values="trade_value",
        title="Exchange Distribution"
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )



# =====================================
# STATUS ANALYSIS
# =====================================

st.divider()

st.header(
    "🚦 Trade Status Monitoring"
)


if not status_df.empty:


    fig = px.pie(
        status_df,
        names="status",
        values="trade_count",
        title="Trade Status Distribution"
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )



# =====================================
# LIVE MARKET FEED
# =====================================

st.divider()

st.header(
    "🔥 Live Market Activity"
)


if not live_df.empty:


    st.caption(
        "Automatically refreshed every 5 seconds"
    )


    st.dataframe(
        live_df.style.format(
            {
                "price": "${:,.2f}",
                "trade_value": "${:,.2f}"
            }
        ),
        use_container_width=True
    )


else:

    st.info(
        "Waiting for live trades..."
    )



# =====================================
# FOOTER
# =====================================

st.divider()

st.caption(
    "Investment Analytics Platform | Kafka Streaming | PostgreSQL Analytics"
)