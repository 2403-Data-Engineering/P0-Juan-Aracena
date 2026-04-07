from Models.StudentModel import StudentModel
from Data.student_dao import *


def add_student(f_name: str, l_name: str, email: str, major: str, year: int) -> StudentModel:

    #Call Student DAO and get dict
    #No need to make email unique. Just use id
    #Return a student object

    create_student(f_name, l_name, email, major, year)

    student = StudentModel(f_name, l_name, email, major, year)
    return student

def remove_student(s_id: int):
    
    #SQL call to check if student is enrolled
    try:
        get_enrollment(s_id)
        delete_student(s_id)

    #Need to search what kind of exception I get when it fails
    except:
        print("Error")

    print("Deleting student...")
    return

def update_student_first_name(id: int, f_name: str):
    
    #SQL call to update student's info
    student = get_student_by_id(id)
    #Compare the name in student with f_name

    #Call this is the name isn't the same
    update_student_f_name(f_name, id)

    print(student)

    return

def update_student_last_name(id: int, l_name: str):
    #SQL call to update student's info

    student = get_student_by_id(id)
    #Compare the name in student with l_name
    #Code goes here

    #Call this is the name isn't the same
    update_student_l_name(l_name, id)

    print(student)

    return

def update_student_email_address(id: int, email: str):
    #SQL call to update student's info

    student = get_student_by_id(id)
    #Compare the name in student with f_name
    #Code goes here

    #Call this is the name isn't the same
    update_student_email(email, id)

    print(student)

    return

def update_student_degree(id: int, major: str):
    #SQL call to update student's info

    student = get_student_by_id(id)
    #Compare the name in student with f_name
    #Code goes here

    #Call this is the name isn't the same
    update_student_major(major, id)

    print(student)

    return

def update_student_grad_year(id: int, year: int):
    #SQL call to update student's info

    student = get_student_by_id(id)
    #Compare the name in student with f_name
    #Code goes here

    #Call this is the name isn't the same
    update_student_year(year, id)

    print(student)

    return

def view_students():
    
    #SQL call to retrieve all the students
    get_all_students()

    return



