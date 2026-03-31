def mainMenu():
    print("""
Welcome to Generic University Admin
1) Create a new student
2) Create a new professor
3) Create a new class
4) Enroll student in class
5) Run report
Q) Quit
          """)
    
    return input("Selection: ").lower()


def studentMenu():
    print("Student menu")
    input("Press Enter to return to the main menu")

    return "menu"

def professorMenu():
    print("Professor menu")
    print("Press Enter to return to the main menu")
    return "menu"

def classMenu():
    print("Class menu")
    print("Press Enter to return to the main menu")
    return "menu"      



def main():
    running = True
    curr_menu = "menu"
    
    while(running):
        match curr_menu:
            case "menu":
                curr_menu = mainMenu()

            case "1":
                curr_menu = studentMenu()

            case "2":
                curr_menu = professorMenu()

            case "3":
                curr_menu = classMenu()

            case "q":
                running = False

if __name__ == "__main__":
    main()