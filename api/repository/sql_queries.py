from shared import MySQLConnector


class MysqlQueries:
    def target_movement_alert(self, conn: MySQLConnector):
        cursor = conn.get_connection().cursor()
        query = """
                SELECT 
                    targets.target_name, 
                    targets.priority_level, 
                    targets.entity_id, 
                    targets.movement_distance_km 
                FROM targets 
                WHERE 
                    (
                    targets.priority_level = 1
                    OR targets.priority_level = 2
                    ) 
                    AND targets.movement_distance_km > 5;
                """
        cursor.execute(query)
        data = cursor.fetchall()
        return data 


