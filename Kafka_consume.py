from kafka import KafkaConsumer

consumer = KafkaConsumer("hello",
bootstrap_servers='8.tcp.ngrok.io:15010'
)
print(consumer._message_generator())
for message in consumer:
    print (message)
