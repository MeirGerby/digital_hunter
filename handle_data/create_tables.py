from shared import log_event, target_bank 
from mysql.connector import MySQLConnection 

class MySQLRepository:
    def __init__(self):
        pass 

    def create_tables(self, connector: MySQLConnection):
        cursor = connector.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS intel" \
            "(" \
                "signal_id VARCHAR(255) PRIMARY KEY, " \
                "timestamp DATETIME," \
                "attack_id VARCHAR(255) FOREIGN KEY," \
                "entity_id VARCHAR(255) FOREIGN KEY," \
                "reported_lat DECIMAL" \
                "reported_lon DECIMAL" \
                "signal_type VARCHAR(255)," \
                "priority_level INT" \
                "distance DECIMAL" \
            ")"
        )
        log_event(level='INFO', message=f"TABLE intel created seccessfully")
        
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS attack" \
            "(" \
                "attack_id VARCHAR(255) PRIMARY KEY," \
                "entity_id VARCHAR(255) FOREIGN KEY," \
                "timestamp DATETIME," \
                "weapon_type VARCHAR(255)" \
            ")"
        )
        log_event(level='INFO', message=f"TABLE attack created seccessfully")

        cursor.execute(
            "CREATE TABLE IF NOT EXISTS damage" \
            "(" \
                "entity_id VARCHAR(255) FOREIGN KEY," \
                "timestamp DATETIME," \
                "attack_id VARCHAR(255) FOREIGN KEY," \
                "result VARCHAR(255)" \
            ")"
        )
        log_event(level='INFO', message=f"TABLE damage created seccessfully")

        cursor.execute(
            "CREATE TABLE IF NOT EXISTS target_bank" \
            "(" \
                "entity_id VARCHAR(255) PRIMARY KEY," \
                "name VARCHAR(255)," \
                "type VARCHAR(255)," \
                "lat DECIMAL" \
                "lon DECIMAL" \
                "priority_level INT" \
                "status VARCHAR(255)"  \
            ")"
        )
        log_event(level='INFO', message=f"TABLE target_bank was created ")
    
    def insert_to_attack(self, values, connector: MySQLConnection):
        """insert data to attack table"""

        cursor = connector.cursor()
        query = "INSERT INTO attack (timestamp, attack_id, entity_id, weapon_type) VALUES (%s, %s, %s, %s)"
        cursor.execute(operation=query, params=values) 
        connector.commit()
        log_event(level='INFO', message=f"{cursor.rowcount}, record inserted.")

    def insert_to_damage(self, values, connector: MySQLConnection):
        """insert data to damage table"""

        cursor = connector.cursor()
        query = "INSERT INTO damage (timestamp, attack_id, entity_id, weapon_type) VALUES (%s, %s, %s, %s)"
        cursor.execute(operation=query, params=values) 
        connector.commit()
        log_event(level='INFO', message=f"{cursor.rowcount}, record inserted.")

    def insert_to_intel(self, values, connector: MySQLConnection):
        """insert data to intel table"""

        cursor = connector.cursor()
        query = "INSERT INTO intel (timestamp, attack_id, entity_id, weapon_type) VALUES (%s, %s, %s, %s)"
        cursor.execute(operation=query, params=values) 
        connector.commit()
        log_event(level='INFO', message=f"{cursor.rowcount}, record inserted.")

    def insert_to_target(self, connector: MySQLConnection):
        """insert data to target table"""
        cursor = connector.cursor()
        for i in target_bank:
            query = "INSERT INTO target (timestamp, attack_id, entity_id, weapon_type) VALUES (%s, %s, %s, %s)"
            cursor.execute(operation=query, params=i) 
        connector.commit()
        log_event(level='INFO', message=f"{cursor.rowcount}, record inserted.")
        
        

