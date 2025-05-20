from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    user_action = {
        "user_id": 101,
        "action": "purchase",
        "timestamp": "2023-10-01T12:00:00"
    }
    producer.send('user_actions', user_action)
    print(f"Sent: {user_action}")
    time.sleep(1)  # Отправляем сообщение каждую секунду
