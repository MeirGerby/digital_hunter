from shared import (
    log_event, 
    ConsumerMessage,
    ProducerMessage,
    DamageSchema,
    AttackSchema,
    IntelSchema, 
    MySQLConnector
)
from .mysql_repository import MySQLRepository

KAFKA_SIGNALS_INTEL_TOPIC = "dlq_signals_intel"
LOG_LEVEL="DEBUG"
KAFKA_GROUP_ID="data"
SIGNAL_TYPES_TOPICS: list[str] = ["intel", "attack", "damage"]
class Manager:
    def __init__(self):
        self.consumer = ConsumerMessage(KAFKA_GROUP_ID) 
        self.producer = ProducerMessage() 
        self.mysql_connector = MySQLConnector().get_connection()
        self.mysql_repository = MySQLRepository()
    
    def data_manager(self, data: dict):
        """the callback function for handling and managing the coming data"""
        try: 
            if "reported_lat" in data:
                # the message is from intel 
                clean_data = IntelSchema(**data).model_dump()
                self.mysql_repository.insert_to_intel(values=clean_data, connector=self.mysql_connector)  # type: ignore

            elif "weapon_type" in data:
                # the message is from airforce attack
                clean_data = AttackSchema(**data).model_dump() 
                self.mysql_repository.insert_to_attack(values=clean_data, connector=self.mysql_connector)  # type: ignore

            elif "result" in data:
                # the message is from damage 
                damage = DamageSchema(**data)
                if damage.result == "destroyed":
                    raise Exception(f"the target {damage.entity_id} already destroyed")
                clean_data = damage.model_dump()
                self.mysql_repository.insert_to_damage(values=clean_data, connector=self.mysql_connector)  # type: ignore
            else:
                log_event(level="Error", message="")
                self.producer.send_message(data=data, topic=KAFKA_SIGNALS_INTEL_TOPIC)
        except Exception as e: 
            log_event(level="Error", message=f"{e}", extra_info=data)
            self.producer.send_message(data=data, topic=KAFKA_SIGNALS_INTEL_TOPIC)


    def main(self):
        """start the program by running the consumer loop"""
        self.mysql_repository.create_tables(self.mysql_connector)    # type: ignore
        self.mysql_repository.insert_to_target(values=clean_data, connector=self.mysql_connector)  # type: ignore
        self.consumer.consumer_loop(self.data_manager, SIGNAL_TYPES_TOPICS) 

if __name__ == "__main__":
    manager = Manager()
    manager.main()
    