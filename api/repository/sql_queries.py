from shared import MySQLConnector
from maps_data import plot_map_with_geometry  


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
                FROM intel_signals
                WHERE intel_signals.priority_level = 99 
                GROUP BY intel_signals.entity_id 
                ORDER BY COUNT(intel_signals.entity_id) DESC 
                LIMIT 3;
                """
        cursor.execute(query)
        data = cursor.fetchall()
        conn.close_connection()
        return data 
    
    def identifying_suspects(self, conn: MySQLConnector):
        """this answer is not correct but i did my best; sorry"""
        cursor = conn.get_connection().cursor(dictionary=True)
        query = """
                SELECT i.entity_id
                FROM intel_signals i 
                WHERE HOUR(i.created_at) BETWEEN 20 AND 8 
                GROUP BY i.entity_id
                HAVING SUM(i.distance_from_last) > 10
                """
        
        cursor.execute(query)
        data = cursor.fetchall()
        conn.close_connection()
        return data 
    
    def get_coords_by_entity_id(self, conn: MySQLConnector, entity_id):
        cursor = conn.get_connection().cursor()
        query = f"""
                SELECT i.reported_lon, i.reported_lat
                FROM intel_signals i 
                WHERE i.entity_id = '{entity_id}' 
                ORDER BY i.timestamp
                """
        
        cursor.execute(query)
        data = cursor.fetchall()
        plot_map_with_geometry(coords=data)
        conn.close_connection()
        return data 
    


if __name__ == "__main__":
    conn = MySQLConnector() 
    query = MysqlQueries().get_coords_by_entity_id(conn, 'TGT-015')
    print(query)




    
