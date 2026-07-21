import csv
from pathlib import Path

from config.logger import get_logger


logger = get_logger(
    "trade_validator",
    "validation.log"
)


PROJECT_ROOT = Path(__file__).resolve().parent.parent

CSV_FILE = PROJECT_ROOT / "data" / "trades.csv"


def main():

    logger.info(
        "Validation started"
    )


    errors = []


    with open(
        CSV_FILE,
        newline="",
        encoding="utf-8"
    ) as file:


        reader = csv.DictReader(file)


        count = 0


        for row in reader:

            count += 1


            if not row["trade_id"]:

                errors.append(
                    "Missing trade id"
                )


            if float(row["price"]) <= 0:

                errors.append(
                    "Invalid price"
                )


            if int(row["quantity"]) <= 0:

                errors.append(
                    "Invalid quantity"
                )


    logger.info(
        f"Records checked: {count}"
    )


    if errors:

        logger.error(
            f"Validation failed: {errors}"
        )

        print(
            "VALIDATION FAILED"
        )

    else:

        logger.info(
            "Validation passed"
        )

        print(
            "VALIDATION PASSED"
        )



if __name__ == "__main__":
    main()