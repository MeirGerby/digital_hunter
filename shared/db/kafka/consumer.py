import json

from confluent_kafka import Consumer

KAFKA_BOOTSTRAP_SERVERS="localhost:9092"
KAFKA_TOPIC=""
class ConsumerMessage:
    def __init__(self, group_id):
        self.config = {
            "bootstrap.servers": KAFKA_BOOTSTRAP_SERVERS,
            "group.id": group_id,
            "auto.offset.reset": "earliest"
        }
        self.consumer = Consumer(self.config)

    def consumer_loop(self, callback, topic):
        self.consumer.subscribe([topic])

        print(f"Consumer is running and subscribed to {topic} topics")

        try:
            while True:
                msg = self.consumer.poll(1.0)
                if msg is None:
                    continue
                if msg.error():
                    print("Error:", msg.error())
                    continue

               
                data = json.loads(msg.value().decode("utf-8")) # type: ignore 
                callback(data) 

        except KeyboardInterrupt:
            print(" the consumer stops by the user")

        finally:
            self.consumer.close()