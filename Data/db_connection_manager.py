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

# def select_message(message: str) -> None:
#     with get_connection() as conn:
#         cursor = conn.cursor(dictionary=True)

#         #Change this later
#         sql = "SELECT * FROM demo_table"

#         cursor.execute(sql)

#         for row in cursor:
#             print(row)

# select_message()

# def get_message_by_id(id: int) -> str:
#     with get_connection() as conn:
#         cursor = conn.cursor(dictionary=True)
#         sql = "SELECT * FROM demo_table WHERE id = %s", 
#         cursor.execute("SELECT * FROM demo_table WHERE id = %s", [id])
#         return cursor.fetchone()

# def create_message(message: str) -> None:
#     with get_connection() as conn:
#         cursor = conn.cursor(dictionary=True)
#         cursor.excecute("INSERT INTO demo_table (message) VALUES (%(message)s)")

# create_message()