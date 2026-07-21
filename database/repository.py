from database.db import get_connection



def save_trade_summary(
        total_trades,
        total_trade_value,
        buy_trades,
        sell_trades
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO trade_summary
        (
            total_trades,
            total_trade_value,
            buy_trades,
            sell_trades
        )
        VALUES (%s,%s,%s,%s)
        """,
        (
            total_trades,
            total_trade_value,
            buy_trades,
            sell_trades
        )
    )

    conn.commit()

    cursor.close()
    conn.close()



def save_symbol_summary(symbol, trade_value):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO symbol_summary
        (
            symbol,
            trade_value
        )
        VALUES (%s,%s)
        """,
        (
            symbol,
            trade_value
        )
    )

    conn.commit()

    cursor.close()
    conn.close()



def save_exchange_summary(exchange, trade_value):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO exchange_summary
        (
            exchange,
            trade_value
        )
        VALUES (%s,%s)
        """,
        (
            exchange,
            trade_value
        )
    )

    conn.commit()

    cursor.close()
    conn.close()



def save_live_trade(trade):

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        INSERT INTO live_trades
        (
            symbol,
            transaction_type,
            quantity,
            price,
            trade_value,
            exchange,
            trade_status
        )
        VALUES
        (%s,%s,%s,%s,%s,%s,%s)
        """,
        (
            trade["symbol"],
            trade["transaction_type"],
            trade["quantity"],
            trade["price"],
            trade["trade_value"],
            trade["exchange"],
            trade["trade_status"]
        )
    )


    conn.commit()

    cursor.close()

    conn.close()