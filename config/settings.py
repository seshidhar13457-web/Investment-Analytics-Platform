"""
Application configuration
Investment Analytics Platform
"""


# Number of trades to generate
NUMBER_OF_TRADES = 100000


# Output configuration

OUTPUT_FOLDER = "data"

OUTPUT_FILE = "trades.csv"


# Stock price ranges

STOCKS = {

    "AAPL": (180, 230),

    "MSFT": (400, 520),

    "GOOGL": (150, 220),

    "AMZN": (170, 250),

    "NVDA": (900, 1400),

    "META": (500, 750),

    "TSLA": (200, 350)

}



# Transaction types

TRANSACTION_TYPES = [

    "BUY",

    "SELL"

]



# Exchanges

EXCHANGES = [

    "NASDAQ",

    "NYSE"

]



# Order types

ORDER_TYPES = [

    "MARKET",

    "LIMIT"

]



# Trade status

TRADE_STATUS = [

    "EXECUTED",

    "PENDING",

    "CANCELLED"

]