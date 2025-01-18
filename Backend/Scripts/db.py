import mysql.connector as mysql_connector
from mysql.connector import errorcode
from logger import *                                # This imports everything from logger.py file..

class SQLConnection:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
    
    def create_Connection(self, attempts = 3, delay = 2):
        attempt = 1

        while attempt <= attempts:
            try:
                return mysql_connector.connect(
                    host = self.host,
                    user = self.user,
                    password = self.password
                )
            
            except (mysql_connector.Error, IOError) as er:

                if (attempts is attempt):   # if 3 = 3
                    logger.info(f"Failed to connect... Exiting without a connection..{er}")
                    return None
                elif er.errno == errorcode.CR_CONNECTION_ERROR:
                    print("Unable to connect. Please check connection params.")
                elif er.errno == errorcode.ER_ACCESS_DENIED_NO_PASSWORD_ERROR:
                    print("Please enter correct password")
                else:
                    logger.info(
                        f"Connection Attempt {attempt} Failed. Error: {er}. Re-trying attempt {attempt + 1}"
                    )
                
                # Progressive reconnect Delay..
                time.sleep(delay ** attempt)
                attempt += 1
            
        return None
    
    def create_Database(self, database):
        self.database = database
        pass
    
    def create_table(self):
        pass
        # self.create_Connection_obj(conn)
        # with conn
    
    def close_Connection(self):
        pass

conn = SQLConnection("localhost", "root", "12345678")
print(conn.create_Connection())
