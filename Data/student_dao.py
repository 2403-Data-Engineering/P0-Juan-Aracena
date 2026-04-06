from db_connection_manager import get_connection

#DAO is data access object
#This is where the SQL code goes
#One DAO per Model
# DAO is where the behavior goes

#User knows their id

def create_student(f_name: str, l_name: str, email: str, major: str, year: int) -> None:
    print("SQL code")


def get_all_students() -> None:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students;")
        
        for row in cursor:
            print(row)

def get_student_by_id(id: int) -> None:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students WHERE s_id = '%s'", (id,))

        for row in cursor:
            print(f"Row goes here: {row}")

def update_student(id: int) -> None:
    print("SQL code")

def remove_student(id: int) -> None:
    print("SQL code")

get_student_by_id(2)