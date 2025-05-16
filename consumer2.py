from kafka import KafkaConsumer, KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda x: x.encode('utf-8')
)

def process_message(message):
    try:
        print(f"Получено сообщение: {message.value.decode('utf-8')}")
    except Exception as e:
        print(f"Ошибка обработки сообщения: {e}")
        producer.send('user_actions_dlt', value=message.value.decode('utf-8'))  # Отправка в DLT

consumer = KafkaConsumer(
    'user_actions',
    bootstrap_servers='localhost:9092',
    group_id='user_actions_group',
    auto_offset_reset='earliest'
)

for message in consumer:
    process_message(message)
