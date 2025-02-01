from Backend.Database.db import SQLConnection
from datetime import date
from dotenv import load_dotenv
import os, json

# import .env file
load_dotenv()

# receive inputs from user
name = input("Please enter your Name : ")
amount = int(input("Please enter the amount : "))
category = input("Please enter category of expense : ")
date = date(input("Please enter the date when the money was spent : "))

print(f'{name} has spent {amount} rupee under Category: {category} on {date}')

# Child class (connection) inherits from parent class.
class connection(SQLConnection):
    def __init__(self, host=os.getenv("host"), user=os.getenv("user"), password=os.getenv("password")):
        super().__init__(host, user, password)
    
    def create_Connection(self, attempts=3, delay=2):
        return super().create_Connection(attempts, delay)
    
    def create_Database(self, database = json.loads(os.environ['databases'])):
        self.database = database
        return super().create_Database(self.database)
    
if __name__ == '__main__':
    c = connection()
    c.create_Connection()
    c.create_Database()
    c.show_databases()
    c.close_connection()