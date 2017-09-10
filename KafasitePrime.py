from kafka import KafkaConsumer
import math

def main():
	consumer = KafkaConsumer('Prime')
	for msg in consumer:
		if prime(msg): print ("This is a prime number:" + msg.value.split(':')[1])

def prime(msg):
	msg = int(msg.value.split(':')[1])
	msgsqrt = math.sqrt(msg)
	for i in xrange(2,msgsqrt):
		if msg% i == 0: return False
	return True

if __name__ == '__main__':
	main()
