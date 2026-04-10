from Models.ClassModel import ClassModel
from Models.StudentModel import StudentModel
from Data.class_dao import *
from Data.student_dao import create_enrollment, delete_enrollment, check_enrollment, get_student_by_id

def add_class(c_name: str, course_code: str, p_id: int) -> None:
    #Check if class exists
    duplicate_class = get_class_by_name(c_name, course_code)

    if len(duplicate_class) > 0:
        print("The class already exists. Try again with a different name or course code")
        return

    c_id = create_class(c_name, course_code, p_id)
    
    new_class = ClassModel(c_name, course_code, p_id)
    
    print("")
    print("Class created:")
    print(f"ID: {c_id}")
    print(f"Class name: {new_class.c_name}")
    print(f"Course code: {new_class.course_code}")
    print(f"Professor ID: {new_class.p_id}")

    return


def change_class_name(c_id: int, c_name: str, course_code: int) -> None:
    duplicate_class = get_class_by_id(c_id)

    #Check if the id the user gave us exists
    if len(duplicate_class) == 0:
        print("Couldn't find class. Enter a valid class ID")
        return
    
    #Check if new name and course code already exist
    duplicate_c_name_code = get_class_by_name(c_name, course_code)
    if len(duplicate_c_name_code) > 0:
        print("Class name and course code already taken. Enter a different class name or course code")
        return
    
    update_class_name(c_name, c_id)
    update_class_course_code(course_code, c_id)

    return
    
def change_class_professor(c_id: int, p_id: int) -> None:
    duplicate_class = get_class_by_id(c_id)

    #Check if the id the user gave us exists
    if len(duplicate_class) == 0:
        print("Couldn't find class. Enter a valid class ID")
        return
    
    update_class_professor(c_id, p_id)

    return

def remove_class(c_id: int) -> None:
    duplicate_class = get_class_by_id(c_id)

    #Check if the id the user gave us exists
    if len(duplicate_class) == 0:
        print("Couldn't find class. Enter a valid class ID")
        return
    
    delete_class(c_id)
    print("Class deleted")

    return

def view_classes() -> list[ClassModel]:
    #  SQL call to retrieve all the classes
    class_list = []

    for row in get_all_classes():
        c_id = row.pop("c_id")
        course = ClassModel(**row)
        course.c_id = c_id
        class_list.append(course)

    return class_list

def view_professor_classes(p_id: int) -> list[ClassModel]:
     
    class_list = []
    for row in get_class_by_professor(p_id):
        c_id = row.pop("c_id")
        course = ClassModel(**row)
        course.c_id = c_id
        class_list.append(course)
    
    return class_list

def enroll_student(s_id: int, c_id: int) -> None:
    
    #Check if the student is already enrolled in the same class
    enrollment = check_enrollment(s_id, c_id)

    if len(enrollment) > 0:
        print("Student is already enrolled in this class. Enter the ID of a different class")
        return
    
    #Check if the student exists
    student = get_student_by_id(s_id)
    if len(student) == 0:
        print("Couldn't find student. Enter a valid student ID")
        return
    
    #Check if the class exists
    duplicate_class = get_class_by_id(c_id)

    #Check if the id the user gave us exists
    if len(duplicate_class) == 0:
        print("Couldn't find class. Enter a valid class ID")
        return

    create_enrollment(s_id, c_id)
    print("\nEnrollment complete")

    
    return


def drop_student(s_id: int, c_id: str) -> None:
    
    #Check if the student exists
    student = get_student_by_id(s_id)
    if len(student) == 0:
        print("Couldn't find student. Enter a valid student ID")
        return
    
    #Check if the class exists
    duplicate_class = get_class_by_id(c_id)

    #Check if the id the user gave us exists
    if len(duplicate_class) == 0:
        print("Couldn't find class. Enter a valid class ID")
        return
    
    #Check if student is enrolled in the given class
    enrollment = check_enrollment(s_id, c_id)

    if len(enrollment) == 0:
        print("The student is not enrolled in the given class. Enter the ID of a different student or a different class")
        return
    
    
    
    delete_enrollment(s_id, c_id)
    print("\nProcess completed")

    return

def view_students_enrolled_in_class(c_id: int) -> list[StudentModel]:
    #Check if the class exists
    duplicate_class = get_class_by_id(c_id)

    #Check if the id the user gave us exists
    if len(duplicate_class) == 0:
        print("Couldn't find class. Enter a valid class ID")
        
        return
    
    students_list = []

    for row in get_all_students_enrolled(c_id):
        s_id = row.pop("s_id")
        student = StudentModel(**row)
        student.s_id = s_id
        students_list.append(student)

    return students_list

def view_all_classes_student_enrolled(s_id: int) -> list[ClassModel]:
    #Check if the student exists
    student = get_student_by_id(s_id)
    if len(student) == 0:
        print("Couldn't find student. Enter a valid student ID")
        return
    
    class_list = []

    for row in get_student_classes(s_id):
        c_id = row.pop("c_id")
        course = ClassModel(**row)
        course.c_id = c_id
        class_list.append(course)

    return class_list