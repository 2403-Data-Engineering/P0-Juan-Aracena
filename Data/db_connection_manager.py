import os
import mysql.connector


from dotenv import load_dotenv
from mysql.connector import Error

load_dotenv()

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("HOST"),
        port=os.getenv("PORT"),
        user=os.getenv("DB_USER"),
        password=os.getenv("PASS"),
        database= os.getenv("DB")
)