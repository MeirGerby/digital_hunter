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
        conn.close_connection()
        return data 
    
    def analysis_collection_sources(self, conn: MySQLConnector):
        cursor = conn.get_connection().cursor()
        query = """
                SELECT 
                    intel_signals.signal_type,
                    COUNT(intel_signals.signal_type) as count_signles
                FROM intel_signals
                GROUP BY 
                    intel_signals.signal_type 
                ORDER BY 
                    COUNT(intel_signals.signal_type) DESC;
                """
        cursor.execute(query)
        data = cursor.fetchall()
        conn.close_connection()
        return data 
    
    def finding_new_targets(self, conn: MySQLConnector):
        cursor = conn.get_connection().cursor()
        query = """
                SELECT 
                    intel_signals.entity_id,
                    COUNT(intel_signals.entity_id) as count_entity
                FROM `intel_signals` 
                WHERE intel_signals.priority_level = 99 
                GROUP BY intel_signals.entity_id 
                ORDER BY COUNT(intel_signals.entity_id) DESC 
                LIMIT 3;
                """
        cursor.execute(query)
        data = cursor.fetchall()
        conn.close_connection()
        return data 

if __name__ == "__main__":
    conn = MySQLConnector() 
    query = MysqlQueries().finding_new_targets(conn)
    print(query)

    
