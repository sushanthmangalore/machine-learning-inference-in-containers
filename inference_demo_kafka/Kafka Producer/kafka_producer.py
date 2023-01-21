from kafka import KafkaProducer
import time
producer = KafkaProducer(bootstrap_servers='localhost:9092')
#Load the document
with open('./sample.txt', 'r') as f:
    text = f.read()
while True:
  producer.send('quickstart-events', text.encode('utf-8'))
  time.sleep(20)