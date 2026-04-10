from dataclasses import dataclass

@dataclass
class ClassModel:
    c_id : int
    c_name : str
    course_code: int
    p_id: int

    def __init__(self, c_name: str, course_code: int, p_id: int):
        self.c_name = c_name
        self.course_code = course_code
        self.p_id = p_id