from database.repository import (
    save_trade_summary,
    save_symbol_summary,
    save_exchange_summary
)


save_trade_summary(
    100,
    500000,
    60,
    40
)


save_symbol_summary(
    "AAPL",
    250000
)


save_exchange_summary(
    "NASDAQ",
    500000
)


print("Data inserted successfully!")