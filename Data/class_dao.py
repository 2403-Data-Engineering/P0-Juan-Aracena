from Data.db_connection_manager import get_connection
from mysql.connector import IntegrityError

def create_class(c_name: str, course_code: str, p_id: int) -> None:
    with get_connection as conn:
        cursor = conn.cursor(dictionary=True)


def select_all_classes() -> None:
    print("SQL code")

#Need to think of what fields a class has
def update_class(c_id: int, c_name: str) -> None:
    print("SQL code")

def delete_class(c_id: int) -> None:
    print("SQL code")
