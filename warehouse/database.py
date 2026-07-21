import psycopg2
import pandas as pd



def get_connection():

    return psycopg2.connect(

        host="localhost",

        database="investment_analytics",

        user="postgres",

        password="Seshidhar@12",

        port="5432"

    )





# ================================
# Warehouse Analytics Queries
# ================================


def get_latest_trade_summary():

    conn = get_connection()

    query = """
    SELECT
        total_trades,
        total_trade_value,
        buy_trades,
        sell_trades,
        created_at
    FROM trade_summary
    ORDER BY created_at DESC
    LIMIT 1
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df





def get_top_symbols():

    conn = get_connection()

    query = """
    SELECT
        symbol,
        trade_value
    FROM symbol_summary
    ORDER BY trade_value DESC
    LIMIT 10
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df





def get_exchange_distribution():

    conn = get_connection()

    query = """
    SELECT
        exchange,
        trade_value
    FROM exchange_summary
    ORDER BY trade_value DESC
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df





def get_trade_status():

    conn = get_connection()

    query = """
    SELECT
        status,
        trade_count
    FROM status_summary
    ORDER BY trade_count DESC
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df





def get_average_trade_size():

    conn = get_connection()

    query = """
    SELECT
        AVG(total_trade_value / total_trades)
        AS average_trade_size
    FROM trade_summary
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df





# ================================
# Connection Test
# ================================


if __name__ == "__main__":

    try:

        conn = get_connection()

        print("Warehouse database connection successful!")

        conn.close()


    except Exception as e:

        print("Warehouse database connection failed:")

        print(e)