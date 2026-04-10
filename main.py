from Service.StudentService import *
from Service.ProfessorService import *
from Service.ClassService import *
from Utils.report_writer import *

def mainMenu():
    print("""
=======================================
Welcome to Generic University Admin
1) Student menu
2) Professor menu
3) Class menu
4) Report menu
Q) Quit
          """)
    
    choice = input("Selection: ").lower()
    print("=======================================")
    
    return choice


def student_menu():
    print(
        """=======================================
Student menu:
1) Add a new student
2) Update a student's information
3) Remove a student from the system
4) View all students
Press "b" to return to the main menu
         """)
    
    
    #User inputs a number to call the function 
    choice = input("Selection: ").lower()
    print("=======================================")
    match choice:
        case "1":
            
            first_name = input("Enter the first name of the student: ").strip().lower()
            last_name = input("Enter the last name of the student: ").strip().lower()
            email = input("Enter the email of the student: ").strip().lower()
            major = input("Enter the major the student studied: ").strip().lower()
            

            year = None
            year_check = True
            while year_check:
                try:
                    year = int(input("Enter the year the student graduated: "))
                    
                    if year > 0:
                        year_check = False

                except ValueError:
                    print("Not an integer value")

            try:

                add_student(first_name, last_name, email, major, year)

            except ValueError:
                return "1"

            return "menu"

        case "2":
            #Make sure the id is a number
            s_id = None

            while s_id is None:
                try:
                    s_id = int(input("Enter the id of the student: "))
                
                except ValueError:
                    print("Not an integer value")

            new_f_name = input("Enter the updated first name: (Press enter to skip) ").strip().lower()
            new_l_name = input("Enter the updated last name: (Press enter to skip) ").strip().lower()
            new_email = input("Enter the updated email: (Press enter to skip) ").strip().lower()
            new_major = input("Enter the updated major: (Press enter to skip) ").strip().lower()
            
            new_year = None
            while new_year is None:
                
                try:
                    new_year = int(input("Enter the updated year: (Press 0 to skip) "))
                
                except ValueError:
                    print("Not an integer value")
            

            if new_f_name:
                update_student_first_name(s_id, new_f_name)
            
            if new_l_name:
                update_student_last_name(s_id, new_l_name)

            if new_email:
                try:
                    update_student_email_address(s_id, new_email)
                except ValueError:
                    return "1"

            if new_major:
                update_student_degree(s_id, new_major)

            if new_year:
                update_student_grad_year(s_id, new_year)

            return "menu"

        case "3":
            s_id = None

            while s_id is None:
                try:
                    s_id = int(input("Enter the ID of the student: "))
                
                except ValueError:
                    print("Not an integer value")
            
            remove_student(s_id)

            return "menu"
            
        case "4":
            students = view_students()

            for index, student in enumerate(students, start=1):
                print("")
                print(f"Student #{index}:")
                print(f"ID: {student.s_id}")
                print(f"First name: {student.f_name}")
                print(f"Last name: {student.l_name}")
                print(f"Email: {student.email}")
                print(f"Major: {student.major}")
                print(f"Year: {student.year}")
            
            return "menu"
        
        case "b":
            return "menu"
        
        case _:
            print("Invalid key entered. Type a number to choose one of the options or 'b' to go back to the main menu")
            return "1"

    return "menu"

def professor_menu():
    print(
        """=======================================
Professor menu:
1) Add a new professor
2) Update a professor's information
3) Remove a professor
4) View all professors
Press "b" to return to the main menu
         """)
    
    choice = input("Selection: ").lower()
    print("=======================================")
    match choice:
        case "1":
            first_name = input("Enter the first name of the professor: ").strip().lower()
            last_name = input("Enter the last name of the professor: ").strip().lower()
            department = input("Enter the department of the professor: ").strip().lower()
            email = input("Enter the email of the professor: ").strip().lower()

            try:
                add_professor(first_name, last_name, department, email)
            
            except ValueError:
                return "2"


            return "menu"

        case "2":
            #Make sure the id is a number
            p_id = None

            while p_id is None:
                try:
                    p_id = int(input("Enter the id of the professor: "))
                
                except ValueError:
                    print("Not an integer value")
            
            new_f_name = input("Enter the updated first name: (Press enter to skip) ").strip().lower()
            new_l_name = input("Enter the updated last name: (Press enter to skip) ").strip().lower()
            new_department = input("Enter the updated department: (Press enter to skip) ").strip().lower()
            new_email = input("Enter the updated email: (Press enter to skip) ").strip().lower()

            if new_f_name:
                update_professor_first_name(p_id, new_f_name)
            
            if new_l_name:
                update_professor_last_name(p_id, new_l_name)

            if new_department:
                update_professor_department(p_id, new_department)

            if new_email:
                try:
                    update_professor_email_address(p_id, new_email)
                except ValueError:
                    return "2"

            return "menu"

        case "3":
            p_id = None

            while p_id is None:
                try:
                    p_id = int(input("Enter the id of the professor: "))
                
                except ValueError:
                    print("Not an integer value")
            
            remove_professor(p_id)

            return "menu"
            
        case "4":
            professors = view_professors()

            for index, professor in enumerate(professors, start=1):
                print("")
                print(f"Professor #{index}:")
                print(f"ID: {professor.p_id}")
                print(f"First name: {professor.f_name}")
                print(f"Last name: {professor.l_name}")
                print(f'Department: {professor.department}')
                print(f"Email: {professor.email}")

            return "menu"
        
        case "b":
            return "menu"
        
        case _:
            print("Invalid key entered. Type a number to choose one of the options or the 'b' to go back to the main menu")
            return "2"

    return "menu"

def class_menu():
    print(
        """=======================================
Class menu:
1) Add a new class
2) Update the details of a class
3) Remove a class
4) View all classes
5) Enroll a student in a class
6) Drop a student from a class
7) View all students enrolled in a class
8) View all classes a given student is enrolled in
Press "b" to return to the main menu
         """)
    
    choice = input("Selection: ").lower()
    print("=======================================")
    match choice:
        case "1":
            class_name = input("Enter the name of the class: ").strip().lower()
            
            course_code = None
            while course_code is None:
                try:
                    course_code = input("Enter the course code: ")
                
                except ValueError:
                    print("Not an integer value")
            
            p_id = None
            while p_id is None:
                try:
                    p_id = input("Enter the ID of the professor you want to assign to this class: ")
                
                except ValueError:
                    print("Not an integer value")

            add_class(class_name, course_code, p_id)

            return "menu"

        case "2":
            c_id = None
            while c_id is None:
                try:
                    c_id = input("Enter the ID of the class: ")
                
                except ValueError:
                    print("Not an integer value")

            new_c_name = ""
            while not new_c_name:
                new_c_name = input("Enter the updated class name: ").strip().lower()

                if not new_c_name:
                    print("Class name cannot be empty. Please enter a valid name.")
                    
            new_course_code = None
            while new_course_code is None:
                
                try:
                    temp_input = int(input("Enter the updated course code: "))

                    if temp_input == 0:
                        print("Course code cannot be 0. Please enter a valid code.")
                        new_course_code = None
                    else:
                        new_course_code = temp_input
                
                except ValueError:
                    print("Not an integer value")
                
            new_p_id = None
            while new_p_id is None:
                try:
                    new_p_id = int(input("Enter the updated professor ID: (Press 0 to skip) "))
                
                except ValueError:
                    print("Not an integer value")
            
            if new_c_name or new_course_code:
                change_class_name(c_id, new_c_name, new_course_code)
               
            if new_p_id:
                change_class_professor(c_id, new_p_id)
            
            print("\nClass updated")

            return "menu"

        case "3":
            c_id = None
            
            while c_id is None:
                try:
                    c_id = int(input("Enter the ID of the class: "))
                
                except ValueError:
                    print("Not an integer value")

            remove_class(c_id)

            return "menu"
            
        case "4":
            class_list = view_classes()

            for index, course in enumerate(class_list, start=1):
                print("")
                print(f"Class #{index}:")
                print(f"ID: {course.c_id}")
                print(f"Class name: {course.c_name}")
                print(f"Course code: {course.course_code}")
                print(f"Professor ID: {course.p_id}")

            return "menu"
        
        case "5":
            s_id = None
            while s_id is None:
                try:
                    s_id = int(input("Enter the ID of the student: "))
                
                except ValueError:
                    print("Not an integer value")
            
            c_id = None
            
            while c_id is None:
                try:
                    c_id = int(input("Enter the ID of the class: "))
                
                except ValueError:
                    print("Not an integer value")

            enroll_student(s_id, c_id)

            return "menu"

        case "6":
            s_id = None
            while s_id is None:
                try:
                    s_id = int(input("Enter the id of the student: "))
                
                except ValueError:
                    print("Not an integer value")
            
            c_id = None
            
            while c_id is None:
                try:
                    c_id = int(input("Enter the ID of the class: "))
                
                except ValueError:
                    print("Not an integer value")

            drop_student(s_id, c_id)

            return "menu"

        case "7":
            c_id = None
            
            while c_id is None:
                try:
                    c_id = int(input("Enter the ID of the class: "))
                
                except ValueError:
                    print("Not an integer value")

            students = view_students_enrolled_in_class(c_id)

            try:
                for index, student in enumerate(students, start=1):
                    print("")
                    print(f"Student #{index}:")
                    print(f"ID: {student.s_id}")
                    print(f"First name: {student.f_name}")
                    print(f"Last name: {student.l_name}")
                    print(f"Email: {student.email}")
                    print(f"Major: {student.major}")
                    print(f"Year: {student.year}")
            
            except TypeError:
                pass

            return "menu"
        
        case "8":
            s_id = None

            while s_id is None:
                try:
                    s_id = int(input("Enter the ID of the student: "))
                
                except ValueError:
                    print("Not an integer value")

            class_list = view_all_classes_student_enrolled(s_id)

            try:
                for index, course in enumerate(class_list, start=1):
                    print("")
                    print(f"Class #{index}:")
                    print(f"ID: {course.c_id}")
                    print(f"Class name: {course.c_name}")
                    print(f"Course code: {course.course_code}")
                    print(f"Professor ID: {course.p_id}")
                
            except TypeError:
                pass

            return "menu"
        
        case "b":
            return "menu"
        
        case _:
            print("Invalid key entered. Type a number to choose one of the options or 'b' to go back to the main menu")
            return "3"
        
    return "menu"      

def report_menu():
    print(
        """=======================================
Report Menu:
1) Generate student enrollment report
2) Generate professor summary report
Press "b" to return to the main menu
""")
    
    choice = input("Selection: ").lower()
    print("=======================================")

    match choice:
        case "1":
            s_id = None
            while s_id is None:
                try:
                    s_id = int(input("Enter the id of the student: "))
                
                except ValueError:
                    print("Not an integer value")
            
            try:
                generate_student_report(s_id)
            except AttributeError:
                pass
            return "menu"
        
        case "2":
            p_id = None

            while p_id is None:
                try:
                    p_id = int(input("Enter the id of the professor: "))
                
                except ValueError:
                    print("Not an integer value")
            
            try:
                generate_professor_report(p_id)
            except AttributeError:
                    pass
            return "menu"
        
        case "b":
            return "menu"
        
        case _:
            print("Invalid key entered. Type a number to choose one of the options or 'b' to go back to the main menu")
            return "4"
        
    return "menu"


def main():
    running = True
    curr_menu = "menu"
    
    while(running):
        match curr_menu:
            case "menu":
                curr_menu = mainMenu()

            case "1":
                curr_menu = student_menu()

            case "2":
                curr_menu = professor_menu()

            case "3":
                curr_menu = class_menu()

            case "4":
                curr_menu = report_menu()

            case "q":
                running = False
                print("Exiting program..")
            
            #Default case for when the user enters a value that isn't any of the specified above
            case _:
                print("Invalid key entered. Type a number to choose one of the options or \"q\" to quit")
                curr_menu = "menu"

if __name__ == "__main__":
    main()