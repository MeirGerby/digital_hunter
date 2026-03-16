from shared import (
    log_event, 
    ConsumerMessage,
    ProducerMessage,
    DamageSchema,
    AttackSchema,
    IntelSchema
)

KAFKA_SIGNALS_INTEL_TOPIC = "dlq_signals_intel"
LOG_LEVEL="DEBUG"
KAFKA_GROUP_ID="data"
SIGNAL_TYPES_TOPICS: list[str] = ["intel", "attack", "damage"]
class Manager:
    def __init__(self):
        self.consumer = ConsumerMessage(KAFKA_GROUP_ID) 
        self.producer = ProducerMessage() 
    
    def data_manager(self, data: dict):
        """the callback function for handling and managing the coming data"""
        try: 
            if "reported_lat" in data:
                
                log_event(level="INFO", message="") 
            elif "weapon_type" in data:
                log_event(level="INFO", message="") 
            elif "result" in data:
                log_event(level="INFO", message="") 
            else:
                log_event(level="Error", message="")
                self.producer.send_message(data=data, topic=KAFKA_SIGNALS_INTEL_TOPIC)
        except Exception as e: 
            log_event(level="Error", message=f"{e}")


    def main(self):
        """start the program by running the consumer loop"""
        self.consumer.consumer_loop(self.data_manager, SIGNAL_TYPES_TOPICS) 

if __name__ == "__main__":
    manager = Manager()
    manager.main()
    