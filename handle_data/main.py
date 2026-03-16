from shared import log_event, ConsumerMessage 

LOG_LEVEL="DEBUG"
KAFKA_GROUP_ID="data"

class Manager:
    def __init__(self):
        self.consumer = ConsumerMessage(KAFKA_GROUP_ID)
    