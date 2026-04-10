from Models.StudentModel import StudentModel
from Data.student_dao import *


def add_student(f_name: str, l_name: str, email: str, major: str, year: int) -> None:

    #Raising value error to the presentation layer
    try:
        s_id = create_student(f_name, l_name, email, major, year)
    except ValueError:
        raise ValueError
    
    student = StudentModel(f_name, l_name, email, major, year)

    print("")
    print("Student created:")
    print(f"ID: {s_id}")
    print(f"First name: {student.f_name}")
    print(f"Last name: {student.l_name}")
    print(f"Email: {student.email}")
    print(f"Major: {student.major}")
    print(f"Year: {student.year}")

    return

def remove_student(s_id: int) -> None:
    
    student = get_student_by_id(s_id)

    #Check if the id the user gave us exists
    if len(student) == 0:
        print("Couldn't find student. Enter a valid student ID")
        return
    
    #Check if the student is enrolled in a class
    enrollments = get_enrollment(s_id)

    if len(enrollments) > 0:
        print("Student is enrolled in one or more classes. Drop the student from the classes or enter a different ID")
        return

    delete_student(s_id)
    print("Student deleted")
    
    return

def update_student_first_name(s_id: int, f_name: str) -> None:
    
    student = get_student_by_id(s_id)

    #Check if the id the user gave us exists
    if len(student) == 0:
        print("Couldn't find student. Enter a valid student ID")
        return

    #Compare the first name in student with f_name
    if student["f_name"] == f_name:
        print("The new first name is the same as the old one. Enter a new first name")
        return

    #Call this is the name isn't the same
    update_student_f_name(f_name, s_id)

    return

def update_student_last_name(s_id: int, l_name: str) -> None:
    
    student = get_student_by_id(s_id)

    #Check if the id the user gave us exists
    if len(student) == 0:
        print("Couldn't find student. Enter a valid student ID")
        return

    #Compare the last name in student with l_name
    if student["l_name"] == l_name:
        print("The new last name is the same as the old one. Enter a new last name")
        return
    #Call this is the name isn't the same
    update_student_l_name(l_name, s_id)

    return

def update_student_email_address(s_id: int, email: str) -> None:
    
    student = get_student_by_id(s_id)

    #Check if the id the user gave us exists
    if len(student) == 0:
        print("Couldn't find student. Enter a valid student ID")
        return
    
    #Compare the email in student with f_name
    if student["email"] == email:
        print("The new email is the same as the old one. Enter a new email")
        return

    #Check if the new enail isn't a duplicate
    try: 
        update_student_email(email, s_id)
    
    except ValueError:
        raise ValueError


    return

def update_student_degree(s_id: int, major: str) -> None:

    student = get_student_by_id(s_id)

    #Check if the id the user gave us exists
    if len(student) == 0:
        print("Couldn't find student. Enter a valid student ID")
        return
    
    #Compare the major in student with major
    if student["major"] == major:
        print("The new major is the same as the old one. Enter a new major")
        return

    #Call this if the major isn't the same
    update_student_major(major, s_id)

    return

def update_student_grad_year(s_id: int, year: int) -> None:
    
    student = get_student_by_id(s_id)

    #Check if the id the user gave us exists
    if len(student) == 0:
        print("Couldn't find student. Enter a valid student ID")
        return
    
    #Compare the year in student with year
    if student["year"] == year:
        print("The new graduation year is the same as the old one. Enter a new graduation year")
        return

    #Call this if the year isn't the same
    update_student_year(year, s_id)

    return

def view_students() -> list[StudentModel]:

    #SQL call to retrieve all the students
    students_list = []

    for row in get_all_students():
        s_id = row.pop("s_id")
        student = StudentModel(**row)
        student.s_id = s_id
        students_list.append(student)

    return students_list

def view_single_student(s_id: int) -> StudentModel:
    student = get_student_by_id(s_id)
    
    #Check if the student exists
    if len(student) == 0:
        print("Couldn't find student. Enter a valid ID")
        return
    
    new_s_id = student.pop("s_id")
    student = StudentModel(**student)
    student.s_id = new_s_id

    return student




