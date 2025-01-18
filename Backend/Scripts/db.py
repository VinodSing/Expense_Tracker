import mysql.connector as mysql_connector
from mysql.connector import errorcode
from logger import *                                # This imports everything from logger.py file..
import os
from dotenv import load_dotenv                      # This imports .env file and all its contents

# parse a .env file and load its variables.
load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")

class SQLConnection:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
    
    def create_Connection(self, attempts = 3, delay = 2):
        attempt = 1
        while attempt <= attempts:
            try:
                self.conn = mysql_connector.connect(
                    host = self.host,
                    user = self.user,
                    password = self.password
                )

                return f"Connected to MySQL instance: {self.conn}"
            
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
    
    def show_databases(self):
        if self.conn and self.conn.is_connected():

            with self.conn.cursor() as cursor:
                show_db = cursor.execute("show databases")
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
            self.conn.close()

    def create_Database(self, database):
        self.database = database

        # accept conn from create_Connection() function
        # If connection is established and db is connected
        if self.conn and self.conn.is_connected():

            with self.conn.cursor() as cursor:
                db_create = cursor.execute(f"create database {self.database}")
            self.conn.close()
    
    def drop_Database(self, database):
        self.database = database

        if self.conn and self.conn.is_connected():

            with self.conn.cursor() as cursor:
                db_drop1 = cursor.execute(f"drop database {self.database}")
            self.conn.close()
    
    def create_table(self):
        pass
    

conn = SQLConnection(host, user, password)
conn.create_Connection()
# conn.create_Database("test")
# conn.drop_Database("test1")
conn.show_databases()
