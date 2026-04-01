def mainMenu():
    print("""
=======================================
Welcome to Generic University Admin
1) Create a new student
2) Create a new professor
3) Create a new class
4) Run report
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
3) Remove a student
4) View all students
Press "b" to return to the main menu
         """)
    
    
    #User inputs a number to call the function 
    choice = input("Selection: ").lower()
    print("=======================================")
    match choice:
        case "1":
            print("Calling create_student function...")
            return "menu"

        case "2":
            print("Calling update_student function...")
            return "menu"

        case "3":
            print("Calling remove_student function...")
            return "menu"
            
        case "4":
            print("Calling view_all_students function...")
            return "menu"
        
        case "b":
            return "menu"
        
        case _:
            print("Invalid key entered. Type a number to choose one of the options or the Enter key to go back to the main menu")
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
            print("Invalid key entered. Type a number to choose one of the options or the Enter key to go back to the main menu")
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
            print("Invalid key entered. Type a number to choose one of the options or the Enter key to go back to the main menu")
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
            print("Invalid key entered. Type a number to choose one of the options or the Enter key to go back to the main menu")
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