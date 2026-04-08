from Models.ProfessorModel import ProfessorModel
from Data.professor_dao import *

def add_professor(f_name: str, l_name: str, department: str, email: str) -> ProfessorModel:
    
    try:
        create_professor(f_name, l_name, department, email)
    
    except ValueError:
        raise ValueError
    
    professor = ProfessorModel(f_name, l_name, department, email)
    
    print("")
    print("Professor created:")
    print(f"ID: {professor.p_id}")
    print(f"First name: {professor.f_name}")
    print(f"Last name: {professor.l_name}")
    print(f"Department: {professor.department}")
    print(f"Email: {professor.email}")

    return 

def remove_professor(p_id: int) -> None:
    
    professor = get_professor_by_id(p_id)

    #Check if the id the user gave us exists
    if len(professor) == 0:
        print("Couldn't find professor. Enter a valid professor ID")
        return

    #Check if the professor has been assigned a class
    classes_assigned = get_class_assigned(p_id)

    if len(classes_assigned) > 0:
        print("Professor is assigned to one or more classes. Remove the professor from the classes or enter a different ID")

    delete_professor(p_id)
    print("Professor deleted")

    return

def update_professor_first_name(p_id: int, f_name: str) -> None:
    
    professor = get_professor_by_id(p_id)

    #Check if the id the user gave us exists
    if len(professor) == 0:
        print("Couldn't find professor. Enter a valid professor ID")
        return

    #Compare the first name in professor with f_name
    if professor["f_name"] == f_name:
        print("The new name is the same as the old one. Enter a new first name")
        return

    #Call this if the first name isn't the same
    update_professor_f_name(f_name, p_id)

    return

def update_professor_last_name(p_id: int, l_name: str) -> None:
    
    professor = get_professor_by_id(p_id)

    #Check if the id the user gave us exists
    if len(professor) == 0:
        print("Couldn't find professor. Enter a valid professor ID")
        return

    #Compare the last name in professor with l_name
    if professor["l_name"] == l_name:
        print("The new name is the same as the old one. Enter a new last name")
        return
    
    #Call this if the last name isn't the same
    update_professor_l_name(l_name, p_id)

    return

def update_professor_department(p_id: int, department: str) -> None:
    professor = get_professor_by_id(p_id)
    
    #Check if the id the user gave us exists
    if len(professor) == 0:
        print("Couldn't find professor. Enter a valid professor ID")
        return
    
    #Compare the department in professor with department
    if professor["department"] == department:
        print("The new department is the same as the old one. Enter a new department")
        return
    
    #Call this if the department isn't the same
    update_professor_dept(department, p_id)

    return

def update_professor_email_address(p_id: int, email: str) -> None:
    
    professor = get_professor_by_id(p_id)

    #Check if the id the user gave us exists
    if len(professor) == 0:
        print("Couldn't find professor. Enter a valid professor ID")
        return
    
    #Compare the email in professor with email
    if professor["email"] == email:
        print("The new email is the same as the old one. Enter a new email")
        return

    #Call this if the email isn't the same
    update_professor_email(email, p_id)

    return

def view_professors() -> None:
    
    #SQL call to get all professors
    professors_list = []

    for row in get_all_professors():
        p_id = row.pop("p_id")
        professor = ProfessorModel(**row)
        professor.p_id = p_id
        professors_list.append(professor)

    return professors_list