from shared import log_event, ConsumerMessage 

LOG_LEVEL="DEBUG"
KAFKA_GROUP_ID="data"
SIGNAL_TYPES_TOPICS: list[str] = ["SIGINT", "VISINT", "HUMINT"]
class Manager:
    def __init__(self):
        self.consumer = ConsumerMessage(KAFKA_GROUP_ID) 
    