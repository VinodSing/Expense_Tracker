import mysql.connector as mysql_connector
from mysql.connector import (connection)
from mysql.connector import errorcode
from dotenv import load_dotenv                      # This imports .env file and all its contents
import time, sys, os

# parse a .env file and load its variables.
load_dotenv()

# Since logger.py is in a different folder, to import this file, 
# first, add the path to sys.path
# second, import logger.py
log_file = os.getenv("log_file_path")
logger_file_path = os.path.join(log_file, 'Backend/Scripts')
sys.path.append(logger_file_path)

from logger import *

class SQLConnection():
    # def __init__(self, host=os.getenv("host"), user=os.getenv("user"), password=os.getenv("password")):
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password

        self.conn = connection.MySQLConnection(
                    user=user,
                    password=password
                )

    # Creates a new Connection object...
    def create_Connection(self, attempts = 3, delay = 2):
        attempt = 1
        while attempt <= attempts:
            try:
                self.conn
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
    
    # Closes existing connection..
    def close_connection(self):
        return self.conn.close()
    
    # Show list of MySQL Databases..
    def show_databases(self):
        print(f"self.conn = {self.conn}")
        print("here....")

        if self.conn.is_connected():
            print("True")
        else:
            print("False")
        if self.conn and self.conn.is_connected():
            with self.conn.cursor() as cursor:
                show_db = cursor.execute("show databases")
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
            # self.conn.close()

    # Creates a database.
    # It takes database in the form of a list passed in .env file..
    def create_Database(self, database):
        self.database = database

        # accept conn from create_Connection() function
        # If connection is established and db is connected

        if self.conn and self.conn.is_connected():
            with self.conn.cursor() as cursor:
                for db in self.database:
                    db_create = cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db}")
                    print(f"Created database : {db}")
            # self.conn.close()
    
    # Drops specified database...
    def drop_Database(self, database):
        self.database = database

        if self.conn and self.conn.is_connected():
            with self.conn.cursor() as cursor:
                db_drop = cursor.execute(f"drop database {self.database}")
            # self.conn.close()
    
    # Creates tables in DB...
    def create_table(self):
        pass

    # Inserts values in the table...
    def insert_into_table(self):
        pass

