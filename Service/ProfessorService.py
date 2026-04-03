from Models.ProfessorModel import ProfessorModel

def create_professor(f_name: str, l_name: str, department: str, email: str) -> ProfessorModel:
    professor = ProfessorModel(f_name, l_name, department, email)

    #SQL 

    return professor

def remove_professor(email: str) -> None:
    #SQL call to remove professor
    return

def update_student(email: str) -> None:
    #SQL call to update professor
    return

def get_all_professors():
    #SQL call to get all professors
    return
