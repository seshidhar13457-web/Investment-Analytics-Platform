import json
from kafka import KafkaConsumer


print("=" * 70)
print(" INVESTMENT ANALYTICS PLATFORM ")
print(" KAFKA TRADE CONSUMER STARTED ")
print("=" * 70)


consumer = KafkaConsumer(
    "investment-trades",
    bootstrap_servers=["127.0.0.1:9092"],
    auto_offset_reset="earliest",
    enable_auto_commit=False,
    group_id=None,
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)



count = 0


for message in consumer:

    trade = message.value

    print("--------------------------------")
    print("Partition:", message.partition)
    print("Offset:", message.offset)
    print("Trade ID:", trade.get("trade_id"))
    print("Symbol:", trade.get("symbol"))

    count += 1

    if count == 10:
        break


consumer.close()


print("=" * 70)
print("TOTAL RECEIVED:", count)
print("=" * 70)