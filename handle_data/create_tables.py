from shared import MySQLConnector 

class MySQLRepository:
    def __init__(self):
        pass 

    def create_tables(self, connector: MySQLConnector):
        cursor = connector.get_cursor()
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
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS attack" \
            "(" \
                "attack_id VARCHAR(255) PRIMARY KEY," \
                "entity_id VARCHAR(255) FOREIGN KEY," \
                "timestamp DATETIME," \
                "weapon_type VARCHAR(255)" \
            ")"
        )
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS damage" \
            "(" \
                "entity_id VARCHAR(255) FOREIGN KEY," \
                "timestamp DATETIME," \
                "attack_id VARCHAR(255) FOREIGN KEY," \
                "result VARCHAR(255)" \
            ")"
        )
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