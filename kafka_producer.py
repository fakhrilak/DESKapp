from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='tcp://8.tcp.ngrok.io:15010')
producer.send('hello', b'Hello, World!')