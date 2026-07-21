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



def fetch_trade_summary():

    conn = get_connection()

    query = """
    SELECT *
    FROM trade_summary
    ORDER BY created_at DESC
    LIMIT 1
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df



def fetch_symbol_summary():

    conn = get_connection()

    query = """
    SELECT symbol, trade_value
    FROM symbol_summary
    ORDER BY trade_value DESC
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df



def fetch_exchange_summary():

    conn = get_connection()

    query = """
    SELECT exchange, trade_value
    FROM exchange_summary
    ORDER BY trade_value DESC
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df



def fetch_status_summary():

    conn = get_connection()

    query = """
    SELECT status, trade_count
    FROM status_summary
    ORDER BY trade_count DESC
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df