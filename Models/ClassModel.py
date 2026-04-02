from dataclasses import dataclass

@dataclass
class ClassModel:
    c_id : int
    class_name : str

    def __init__(self, class_name: str):
        self.class_name = class_name