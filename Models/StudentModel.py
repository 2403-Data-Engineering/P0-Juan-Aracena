#Imports the dataclass decorator from the dataclass module
from dataclasses import dataclass

# Tells Python to treat the class as a data container
@dataclass
class StudentModel:
    s_id : int
    f_name : str
    l_name : str
    email : str
    major : str
    year : int

    def __init__(self, f_name: str, l_name: str, email: str, major: str, year: int):
        self.f_name = f_name
        self.l_name = l_name
        self.email = email
        self.major = major
        self.year = year
            
