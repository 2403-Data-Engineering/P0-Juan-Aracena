from Data.db_connection_manager import get_connection
from mysql.connector import IntegrityError 

def create_professor(f_name: str, l_name: str, department: str, email: str) -> None:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)

        try:
            cursor.execute("INSERT INTO professors(f_name, l_name, department, email) VALUES (%s, %s, %s, %s)", (f_name, l_name, department, email))

        except IntegrityError:
            print("\nDuplicate email found. Enter a different email")
            raise ValueError

        conn.commit()

def get_all_professors() -> None:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM professors;")
        
        return cursor.fetchall()

def get_professor_by_id(p_id: int) -> dict[int, str, str, str, str]:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM professors WHERE p_id = '%s'", (p_id,))

        professor = dict()
        for row in cursor:
            professor = row
        
    return professor

def get_class_assigned(p_id: int) -> dict[int, str, str, str, str]:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True) 
        cursor.execute("SELECT * FROM classes where p_id = %s", (p_id, ))

        classes_assigned = dict()
        for row in cursor:
            classes_assigned = row
        
        return classes_assigned
    
def update_professor_f_name(f_name: str, p_id: int) -> None:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("UPDATE professors SET f_name = %s WHERE p_id = %s", (f_name, p_id))
    
        conn.commit()

def update_professor_l_name(l_name: str, p_id: int) -> None:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("UPDATE professors SET l_name = %s WHERE p_id = %s", (l_name, p_id))

        conn.commit()

def update_professor_dept(department: str, p_id: int) -> None:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("UPDATE professors SET department = %s WHERE p_id = %s", (department, p_id))

        conn.commit()

def update_professor_email(email: str, p_id: int) -> None:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("UPDATE professors SET email = %s WHERE p_id = %s", (email, p_id))

        conn.commit()
    
def delete_professor(p_id: int) -> None:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("DELETE FROM professors WHERE p_id = %s", (p_id, ))

        conn.commit()


