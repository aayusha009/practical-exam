import json
import time
from kafka import KafkaProducer



producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

orders = [
    {"order_id": 1, "customer_id": 101, "status": "delivered"},
    {"order_id": 2, "customer_id": 102, "status": "shipped"},
    {"order_id": 3, "customer_id": 103, "status": "delivered"},

]
for order in orders:
    producer.send("orders",order)
    print("sent")
    time.sleep(1)