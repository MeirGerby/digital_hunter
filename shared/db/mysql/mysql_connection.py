from mysql.connector import connect, MySQLConnection

MYSQL_HOST = "localhost"
MYSQL_USER= "root" 
MYSQL_PORT=3306
MYSQL_PASSWORD = "password" 
MYSQL_DATABASE = "data"

class MySQLConnector:
    def get_connection(self):
        self.mydb = connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD, 
            database=MYSQL_DATABASE,
            port=MYSQL_PORT
        )
        return self.mydb
        

    def get_cursor(self):
        return self.mydb.cursor(dictionary=True) # type: ignore
    
    def close_connection(self):
        if self.mydb:
            return self.mydb.close
    

