from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
i = 0
while True:
	producer.send('Prime',"The Number is :" +str(i))
	i += 1
