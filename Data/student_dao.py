from Data.db_connection_manager import get_connection
from mysql.connector import IntegrityError


#DAO is data access object
#This is where the SQL code goes
#One DAO per Model
# DAO is where the behavior goes

#User knows their id

#Might need to return s_id
# cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", ("Alice", "alice@example.com"))
# conn.commit()
# new_id = cursor.lastrowid
 
def create_student(f_name: str, l_name: str, email: str, major: str, year: int) -> int:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)

        try:
            cursor.execute("INSERT INTO students(f_name, l_name, email, major, year) VALUES (%s, %s, %s, %s, %s)", (f_name, l_name, email, major, year))

        except IntegrityError:
            print("\nDuplicate email found. Enter a different email")
            raise ValueError

        conn.commit()
        new_id = cursor.lastrowid
    
    return new_id

def get_all_students() -> list[dict]:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students;")
        
        return cursor.fetchall()

def get_student_by_id(s_id: int) -> dict[int, str, str, str, str, int]:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students WHERE s_id = '%s'", (s_id,))

        student = dict()
        for row in cursor:
            student = row
        
    return student

#Service layer in ClassService will check for duplicate
def create_enrollment(s_id: int, c_id: int) -> None:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("INSERT INTO enrollment(s_id, c_id) VALUES (%s, %s)", (s_id, c_id))

        conn.commit()

def delete_enrollment(s_id: int, c_id: int) -> None:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("DELETE FROM enrollment WHERE s_id = %s AND c_id = %s", (s_id, c_id))

        conn.commit()


def get_enrollment(s_id: int) -> dict[int, str, str, str, str, int]:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True) 
        cursor.execute("SELECT * FROM enrollment where s_id = %s", (s_id, ))

        enrollment = dict()
        for row in cursor:
            enrollment = row
        
        return enrollment

def check_enrollment(s_id: int, c_id: int) -> dict[int, str, int, int]:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM enrollment WHERE s_id = %s AND c_id = %s", (s_id, c_id))

        enrollment = dict()
        for row in cursor:
            enrollment = row
        
        return enrollment
    

def update_student_f_name(f_name: str, s_id: int) -> None:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("UPDATE students SET f_name = %s WHERE s_id = %s", (f_name, s_id))
    
        conn.commit()

def update_student_l_name(l_name: str, s_id: int) -> None:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("UPDATE students SET l_name = %s WHERE s_id = %s", (l_name, s_id))

        conn.commit()

def update_student_email(email: str, s_id: int) -> None:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)

        try:
            cursor.execute("UPDATE students SET email = %s WHERE s_id = %s", (email, s_id))
            conn.commit()

        except IntegrityError:
            print("\nDuplicate email found. Enter a different email")
            raise ValueError
        
    return

def update_student_major(major: str, s_id: int) -> None:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("UPDATE students SET major = %s WHERE s_id = %s", (major, s_id))

        conn.commit()

def update_student_year(year: int, s_id: int) -> None:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("UPDATE students SET year = %s WHERE s_id = %s", (year, s_id))

        conn.commit()

def delete_student(s_id: int) -> None:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("DELETE FROM students WHERE s_id = %s", (s_id, ))

        conn.commit()
