import json
from kafka import KafkaConsumer


consumer = KafkaConsumer (
    bootstrap_servers="localhost:9092",
    group_id="q8-consumer-group",
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
    auto_offset_reset="earliest",
    )

print("waiting for orders")

for message in consumer:
    print(
        f"partition={message.partition} "
        f"offset={message.offset} "
        f"key={message.key} "
        f"value={message.value}"
    )
