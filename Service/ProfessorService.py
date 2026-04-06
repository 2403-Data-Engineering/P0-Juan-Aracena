from Models.ProfessorModel import ProfessorModel
from Data.professor_dao import *

def add_professor(f_name: str, l_name: str, department: str, email: str) -> ProfessorModel:
    
    create_professor(f_name, l_name, department, email)
    professor = ProfessorModel(f_name, l_name, department, email)
    return professor

def remove_professor(email: str) -> None:
    #SQL call to remove professor
    return

#First, get a professor by using their id. Then, update the info
def update_professor(p_id: int, f_name: str, l_name: str, department: str, email: str) -> None:
    #SQL call to update professor
    return

def get_all_professors() -> None:
    #SQL call to get all professors
    return
