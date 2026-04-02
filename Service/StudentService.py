#Move this import to presentation after setting up database and testing dummy data
from Models.StudentModel import StudentModel

#Dummy data
# student1 = StudentModel(1, "John", "Doe", "john@gmail.com", "computer science", 2015)
# student2 = StudentModel(2, "James", "Smith", "james@gmail.com", "biology", 2020)
# student3 = StudentModel(3, "Paul", "Bond", "paul@gmail.com", "history", 2010)

# student_lst = [student1, student2, student3]

def create_student(f_name: str, l_name: str, email: str, major: str, year: int) -> StudentModel:

    #Make SQL calls here
    #Might need to add a unique constraint to email

    student = StudentModel(f_name, l_name, email, major, year)
    print("Calling DB to create a new student...")
    return student

#Change arguments in case I decide to not add a unique constraint to emails
def remove_student(email):
    
    #SQL call to retrieve student using the given email goes here
    
    print("Deleting student...")
    return


