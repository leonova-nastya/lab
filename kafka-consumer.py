from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'user_actions',
    bootstrap_servers='localhost:9092',
    group_id='user_actions_group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

action_count = {}
total_messages = 0

for message in consumer:
    action = message.value['action']
    total_messages += 1
    
    if action == "purchase":
        action_count[action] = action_count.get(action, 0) + 1
        
    print(f"Received: {message.value}")

print(f"Total messages processed: {total_messages}")
print(f"Action counts: {action_count}")
