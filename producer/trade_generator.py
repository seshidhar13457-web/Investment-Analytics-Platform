import csv
import os
import random
import time

from datetime import datetime, timedelta

from faker import Faker

from config.settings import (
    NUMBER_OF_TRADES,
    OUTPUT_FOLDER,
    OUTPUT_FILE,
    STOCKS,
    TRANSACTION_TYPES,
    EXCHANGES,
    ORDER_TYPES,
    TRADE_STATUS,
)

from config.logger import get_logger


fake = Faker()


logger = get_logger(
    "trade_generator",
    "generator.log"
)



def generate_trade(writer, trade_id):

    symbol = random.choice(
        list(STOCKS.keys())
    )


    min_price, max_price = STOCKS[symbol]


    price = round(
        random.uniform(
            min_price,
            max_price
        ),
        2
    )


    quantity = random.randint(
        1,
        500
    )


    trade_value = round(
        quantity * price,
        2
    )


    trade_time = (
        datetime.now()
        -
        timedelta(
            days=random.randint(0,30),
            hours=random.randint(0,23)
        )
    )


    writer.writerow([

        trade_id,

        f"PORT{random.randint(1000,9999)}",

        f"INV{random.randint(10000,99999)}",

        fake.name(),

        symbol,

        random.choice(EXCHANGES),

        random.choice(TRANSACTION_TYPES),

        random.choice(ORDER_TYPES),

        random.choice(TRADE_STATUS),

        quantity,

        price,

        trade_value,

        trade_time.strftime(
            "%Y-%m-%d %H:%M:%S"
        )

    ])





def main():

    start_time = time.time()


    os.makedirs(
        OUTPUT_FOLDER,
        exist_ok=True
    )


    output_path = os.path.join(
        OUTPUT_FOLDER,
        OUTPUT_FILE
    )


    logger.info(
        "Large trade generation started"
    )


    with open(
        output_path,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:


        writer = csv.writer(file)


        writer.writerow([

            "trade_id",
            "portfolio_id",
            "investor_id",
            "investor_name",
            "symbol",
            "exchange",
            "transaction_type",
            "order_type",
            "trade_status",
            "quantity",
            "price",
            "trade_value",
            "trade_timestamp"

        ])



        for trade_id in range(
            1,
            NUMBER_OF_TRADES + 1
        ):

            generate_trade(
                writer,
                trade_id
            )


    end_time = time.time()


    duration = round(
        end_time - start_time,
        2
    )


    logger.info(
        f"Generated {NUMBER_OF_TRADES} trades"
    )


    logger.info(
        f"Generation time: {duration} seconds"
    )


    print("=" * 70)

    print("TRADE GENERATION COMPLETE")

    print(
        f"Generated {NUMBER_OF_TRADES:,} trades"
    )

    print(
        f"Time taken: {duration} seconds"
    )

    print(
        f"Saved: {output_path}"
    )

    print("=" * 70)




if __name__ == "__main__":
    main()