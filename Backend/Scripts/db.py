import mysql.connector as mysql_connector
from mysql.connector import errorcode
import pymysql

class SQLConnection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
    
    def create_Connection_obj(self):
        try:
            connection = mysql_connector.connect(
                self.host,
                self.user,
                self.password
            )
        except mysql_connector.Error as er:
            if er.errno == errorcode.CR_CONNECTION_ERROR:
                print("Unable to connect. Please check connection params.")
            elif er.errno == errorcode.ER_ACCESS_DENIED_NO_PASSWORD_ERROR:
                print("Please enter correct password")
            else:
                print(er)
        
        else:
           connection.close() 
    
    def create_table(self):
        pass
        # self.create_Connection_obj(conn)
        # with conn

