from dataclasses import dataclass

@dataclass
class ClassModel:
    c_id : int
    class_name : str
    course_code: int
    p_id: int

    def __init__(self, class_name: str, course_code: int, p_id: int):
        self.class_name = class_name,
        self.course_code = course_code
        self.p_id = p_id