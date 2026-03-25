from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    data = {
        "ride_id": random.randint(1, 10000),
        "distance": round(random.uniform(1, 20), 2),
        "fare": round(random.uniform(5, 50), 2),
        "timestamp": datetime.utcnow().isoformat()
    }

    producer.send("rides", data)
    print("Sent:", data)
    time.sleep(2)