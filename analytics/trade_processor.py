import json

from kafka import KafkaConsumer

from analytics.metrics import TradeMetrics


KAFKA_SERVER = "127.0.0.1:9092"

TOPIC = "investment-trades"


print("=" * 70)

print(" INVESTMENT ANALYTICS ENGINE ")

print("=" * 70)



consumer = KafkaConsumer(

    bootstrap_servers=[KAFKA_SERVER],

    auto_offset_reset="earliest",

    enable_auto_commit=False,

    group_id=None,

    value_deserializer=lambda x: json.loads(
        x.decode("utf-8")
    )

)



print("Kafka consumer connected successfully")



consumer.subscribe([TOPIC])



while not consumer.assignment():

    consumer.poll(timeout_ms=1000)



print("Assigned partitions:")

for partition in consumer.assignment():

    print(partition)



consumer.seek_to_beginning()



metrics = TradeMetrics()


count = 0



while True:


    records = consumer.poll(

        timeout_ms=1000,

        max_records=500

    )


    if not records:

        break



    for partition, messages in records.items():


        for message in messages:


            trade = message.value


            metrics.process_trade(trade)


            count += 1



            if count % 10000 == 0:

                print(
                    f"Processed {count} trades"
                )



consumer.close()



print("=" * 70)

print(
    f"TOTAL TRADES PROCESSED: {count}"
)

print("=" * 70)



# Display analytics report

metrics.report()



# Save analytics into PostgreSQL

metrics.save_to_database()