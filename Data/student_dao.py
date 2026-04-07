from Data.db_connection_manager import get_connection

#DAO is data access object
#This is where the SQL code goes
#One DAO per Model
# DAO is where the behavior goes

#User knows their id

#Might need to return s_id
# cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", ("Alice", "alice@example.com"))
# conn.commit()
# new_id = cursor.lastrowid
 
#Can there be duplicate students?
def create_student(f_name: str, l_name: str, email: str, major: str, year: int) -> None:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("INSERT INTO students(f_name, l_name, email, major, year) VALUES (%s, %s, %s, %s, %s)", (f_name, l_name, email, major, year))
        
        conn.commit()

def get_all_students() -> None:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students;")
        
        for row in cursor:
            print(row)

def get_student_by_id(id: int) -> dict[int, str, str, str, str, int]:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students WHERE s_id = '%s'", (id,))

        student = dict()
        for row in cursor:
            # print(f"Row goes here: {row}")
            student = row
        
        return student

def get_enrollment(s_id: int) -> None:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True) 
        cursor.execute("SELECT * FROM enrollment where s_id = %s", (s_id, ))


#Service layer will handle the case where the user enters the same info that's in the db
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
        cursor.execute("UPDATE students SET email = %s WHERE s_id = %s", (email, s_id))

        conn.commit()

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

#Presentation layer will make sure that the student won't get deleted if they're enrolled
def delete_student(s_id: int) -> None:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("DELETE FROM students WHERE s_id = %s", (s_id, ))

        conn.commit()

# create_student("Alice", "Jane", "alice@gmail.com", "history", 2000)
# update_student(1)