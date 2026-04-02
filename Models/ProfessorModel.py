from dataclasses import dataclass

@dataclass
class ProfessorModel:
    p_id : int
    f_name: str
    l_name: str
    department: str
    email: str

    def __init__(self, f_name: str, l_name: str, department: str, email: str):
        self.f_name = f_name
        self.l_name = l_name
        self.department = department
        self.email = email