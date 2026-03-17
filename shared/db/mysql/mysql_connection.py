from mysql.connector import connect, MySQLConnection
from shared.core.settings import config 
MYSQL_HOST = config.MYSQL_HOST
MYSQL_USER = config.MYSQL_USER
MYSQL_PORT = config.MYSQL_PORT
MYSQL_PASSWORD = config.MYSQL_PASSWORD
MYSQL_DATABASE = config.MYSQL_DATABASE

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
    

