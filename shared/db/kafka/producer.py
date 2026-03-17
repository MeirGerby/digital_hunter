import json
from confluent_kafka import Producer
from shared.logging import log_event


KAFKA_BOOTSTRAP_SERVERS="localhost:9092" 

class ProducerMessage:
    def __init__(self):
        self.config = {
            "bootstrap.servers": KAFKA_BOOTSTRAP_SERVERS
        }

        self.producer = Producer(self.config)

    def delivery_report(self, err, msg):
        if err:
            log_event(level="ERROR", message=f"Delivery failed: {err}")
        else:
            log_event(level="INFO", message=f"Delivered {msg.value().decode('utf-8')}")


    def send_message(self, data, topic):
        try:
            self.producer.produce(
                topic=topic,
                value=json.dumps(data).encode("utf-8"),
                callback=self.delivery_report
            )
        finally:
            self.producer.flush()