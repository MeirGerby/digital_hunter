from shared import log_event, ConsumerMessage 

LOG_LEVEL="DEBUG"
KAFKA_GROUP_ID="data"
SIGNAL_TYPES_TOPICS: list[str] = ["intel", "attack", "damage"]
class Manager:
    def __init__(self):
        self.consumer = ConsumerMessage(KAFKA_GROUP_ID)  
    
    def data_manager(self):
        """the callback function for handling and managing the coming data"""
        pass 

    def main(self):
        """start the program by running the consumer loop"""
        self.consumer.consumer_loop(SIGNAL_TYPES_TOPICS, self.data_manager) 

if __name__ == "__main__":
    manager = Manager()
    manager.main()
    