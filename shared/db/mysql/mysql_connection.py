from mysql.connector import connect, MySQLConnection

MYSQL_HOST = "localhost"
MYSQL_USER= "root" 
MYSQL_PASSWORD = "password" 
MYSQL_DATABASE = "data"

class MySQLConnector:
    def __init__(self) -> None:
        self.mydb: MySQLConnection | None = None 

    def get_connection(self):
        self.mydb = connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD, 
            database=MYSQL_DATABASE
        )
    
    def close_connection(self):
        if self.mydb:
            return self.mydb.close()
    

