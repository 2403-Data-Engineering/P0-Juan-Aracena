from Data.db_connection_manager import get_connection
from mysql.connector import IntegrityError

def create_class(c_name: str, course_code: str, p_id: int) -> int:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)

        try:
            cursor.execute("INSERT INTO classes(c_name, course_code, p_id) VALUES (%s, %s, %s)", (c_name, course_code, p_id))

        except IntegrityError:
            print("\nDuplicate class. Enter a different class name and code")
            raise ValueError
        
        conn.commit()
        new_id = cursor.lastrowid
    
    return new_id


def get_all_classes() -> list[dict]:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM classes;")
        
        return cursor.fetchall()

# View all students enrolled in a class
def get_all_students_enrolled(c_id: int) -> list[dict]:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT s.s_id, s.f_name, s.l_name, s.email, s.major, s.year FROM classes c INNER JOIN enrollment e on c.c_id = e.c_id INNER JOIN students s on e.s_id = s.s_id WHERE c.c_id = %s;", (c_id, ))

        return cursor.fetchall()

# View all classes a given student is enrolled in
def get_student_classes(s_id: int) -> list[dict]:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT c.c_id, c.c_name, c.course_code, c.p_id FROM enrollment e INNER JOIN students s on e.s_id = s.s_id INNER JOIN classes c on e.c_id = c.c_id WHERE e.s_id = %s", (s_id, ))

        return cursor.fetchall()

def get_class_by_id(c_id: int) -> dict[int, str, int, int]:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM classes WHERE c_id = %s", (c_id, ))

        curr_class = dict()
        for row in cursor:
            curr_class = row
        
    return curr_class

def get_class_by_professor(p_id: int) -> list[dict]:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT c.c_id, c.c_name, c.course_code, c.p_id FROM classes c inner join professors p on c.p_id = p.p_id WHERE c.p_id = %s", (p_id, ))

        return cursor.fetchall()
    
def get_class_by_name(c_name: str, course_code: int) -> dict[int, str, int, int]:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM classes WHERE c_name = %s AND course_code = %s", (c_name, course_code))

        duplicate_class = dict()
        for row in cursor:
            duplicate_class = row
        
        return duplicate_class

def update_class_name(c_name: str, c_id: int) -> None:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("UPDATE classes SET c_name = %s WHERE c_id = %s", (c_name, c_id))
    
        conn.commit()

def update_class_course_code(course_code: str, c_id: int) -> None:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("UPDATE classes SET course_code = %s WHERE c_id = %s", (course_code, c_id))
    
        conn.commit()

def update_class_professor(p_id: int, c_id: int) -> None:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("UPDATE classes SET p_id = %s WHERE p_id = %s", (p_id, c_id))
    
        conn.commit()

def delete_class(c_id: int) -> None:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("DELETE FROM classes WHERE c_id = %s", (c_id, ))

        conn.commit()