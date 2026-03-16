from mysql.connector import connect, MySQLConnection

MYSQL_HOST = "localhost"
MYSQL_USER= "root" 
MYSQL_PASSWORD = "password" 
MYSQL_DATABASE = "data"

class MySQLConnector:
    def __init__(self) -> None:
        self.mydb = connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD, 
            database=MYSQL_DATABASE
        )

    def get_cursor(self):
        return self.mydb.cursor(dictionary=True) # type: ignore
    
    def close_connection(self):
        if self.mydb:
            return self.mydb.close
    

