from Service.StudentService import *

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
            last_name = input('Enter the last name of the student: ').strip().lower()
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
                    new_year = int(input("Enter the updated year: (Press 0 to skip) ")).strip()
                
                except ValueError:
                    print("Not an integer value")
            

            if new_f_name:
                update_student_first_name(s_id, new_f_name)
            
            if new_l_name:
                update_student_last_name(s_id, new_l_name)

            if new_email:
                update_student_email(s_id, new_email)

            if new_major:
                update_student_major(s_id, new_major)

            if new_year:
                update_student_grad_year(s_id, new_year)

            return "menu"

        case "3":
            s_id = None

            while s_id is None:
                try:
                    s_id = int(input("Enter the id of the student: "))
                
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
            print("Calling create_professor function...")
            return "menu"

        case "2":
            print("Calling update_professor function...")
            return "menu"

        case "3":
            print("Calling remove_professor function...")
            return "menu"
            
        case "4":
            print("Calling view_all_professors function...")
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
Press "b" to return to the main menu
         """)
    
    choice = input("Selection: ").lower()
    print("=======================================")
    match choice:
        case "1":
            print("Calling create_class function...")
            return "menu"

        case "2":
            print("Calling update_class function...")
            return "menu"

        case "3":
            print("Calling remove_class function...")
            return "menu"
            
        case "4":
            print("Calling view_all_classes function...")
            return "menu"
        
        case "5":
            print("Calling enroll_student function")
            return "menu"

        case "6":
            print("Calling drop_student function")
            return "menu"

        case "7":
            print("Calling view_students_in_class function")
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
            print("Calling generate_student_report function")
            return "menu"
        
        case "2":
            print("Calling generate_professor_report function")
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