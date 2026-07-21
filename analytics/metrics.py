from collections import defaultdict

from database.repository import (
    save_trade_summary,
    save_symbol_summary,
    save_exchange_summary,
    save_live_trade
)



class TradeMetrics:


    def __init__(self):

        self.total_trades = 0
        self.total_value = 0.0

        self.buy_trades = 0
        self.sell_trades = 0

        self.symbol_values = defaultdict(float)

        self.exchange_values = defaultdict(float)

        self.status_count = defaultdict(int)



    def process_trade(self, trade):

        self.total_trades += 1


        trade_value = float(
            trade["trade_value"]
        )


        self.total_value += trade_value



        if trade["transaction_type"] == "BUY":

            self.buy_trades += 1

        else:

            self.sell_trades += 1



        self.symbol_values[
            trade["symbol"]
        ] += trade_value



        self.exchange_values[
            trade["exchange"]
        ] += trade_value



        self.status_count[
            trade["trade_status"]
        ] += 1



        # save latest trade

        save_live_trade(trade)



    def save_to_database(self):

        save_trade_summary(
            self.total_trades,
            self.total_value,
            self.buy_trades,
            self.sell_trades
        )


        for symbol,value in self.symbol_values.items():

            save_symbol_summary(
                symbol,
                value
            )


        for exchange,value in self.exchange_values.items():

            save_exchange_summary(
                exchange,
                value
            )


        print(
            "Analytics saved to PostgreSQL"
        )