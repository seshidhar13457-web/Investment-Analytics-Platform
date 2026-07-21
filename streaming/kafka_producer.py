import csv
import json
import time

from kafka import KafkaProducer


KAFKA_SERVER = "127.0.0.1:9092"
TOPIC_NAME = "investment-trades"

CSV_FILE = "data/trades.csv"


print("=" * 70)
print(" INVESTMENT ANALYTICS PLATFORM ")
print(" KAFKA TRADE PRODUCER STARTED ")
print("=" * 70)


producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    value_serializer=lambda value: json.dumps(value).encode("utf-8")
)


sent_count = 0


with open(CSV_FILE, mode="r", encoding="utf-8") as file:

    reader = csv.DictReader(file)

    for trade in reader:

        producer.send(
            TOPIC_NAME,
            value=trade
        )

        sent_count += 1

        if sent_count % 1000 == 0:
            print(f"Sent {sent_count} trades")

        # simulate real-time streaming speed
        time.sleep(0.01)


producer.flush()

producer.close()


print("=" * 70)
print(" KAFKA PRODUCER COMPLETE ")
print(f" TOTAL TRADES SENT: {sent_count}")
print("=" * 70)