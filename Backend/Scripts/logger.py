import logging
import time
import mysql.connector

# Set up logger
logger = logging.getLogger(__name__) #Logger name tracks package/module hierachy
logger.setLevel(logging.INFO)

# display logger message on Console
stream_Handler = logging.StreamHandler()   # sends logging output to streams such as sys.stdout, sys.stderr, etc
logger.addHandler(stream_Handler)

# Log output in a file
file_Handler = logging.FileHandler("/Users/vimita/Documents/Data_Eng_Projects/Expense_Tracker/Backend/log_files/err_log.log") 
logger.addHandler(file_Handler)

