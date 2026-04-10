from yattag import Doc
from Service.StudentService import view_single_student
from Service.ClassService import view_all_classes_student_enrolled, view_professor_classes, view_students_enrolled_in_class
from Service.ProfessorService import view_single_professor



def generate_student_report(s_id: int, filename="Utils/reports/student_report.html") -> None:
    
    #Get student info
    student = view_single_student(s_id)

    #Return to main.py if it can't find the student
    if student is None:
        return

    #Get all the classes the student is enrolled in
    class_list = view_all_classes_student_enrolled(s_id)

    doc, tag, text = Doc().tagtext()

    doc.asis('<DOCTYPE! html>')
    
    with tag('html'):
        with tag('head'):
            with tag('title'):
                text('Student Enrollment Report')
        
        with tag('body'):
            with tag('h1'):
                text(f"{student.f_name.capitalize()}'s Enrollment Report")
            
            with tag('p'):
                with tag('b'):
                    text(f'First name: ')
                
                text(student.f_name.capitalize())

            with tag('p'):
                with tag('b'):
                    text(f'Last name: ')
                
                text(student.l_name.capitalize())

            with tag('p'):
                with tag('b'):
                    text(f'Email: ')
                
                text(student.email)

            with tag('p'):
                with tag('b'):
                    text(f'Major: ')
                
                text(student.major.capitalize())

            with tag('p'):
                with tag('b'):
                    text(f'Graduation year: ')
                
                text(student.year)
            
            with tag('h2'):
                text('Classes:')

            with tag('ul'):
                #Get professor name for each p_id in the class list
                professor_list = []
                for index, course in enumerate(class_list):
                    professor = view_single_professor(course.p_id)

                    professor_list.append(professor)

                    with tag('li'):
                        with tag('b'):
                            text('Class name: ')
                        text(course.c_name.capitalize())
                        doc.stag('br')
                        doc.stag('br')

                        with tag('b'):
                            text('Course code: ')
                        text(course.course_code)
                        doc.stag('br')
                        doc.stag('br')

                        with tag('b'):
                            text('Professor: ')
                        text(f'{professor_list[index].f_name.capitalize()} {professor_list[index].l_name.capitalize()}')
                    doc.stag('br')
                    doc.stag('br')
                    
                       
    with open(filename, "w") as w_file:
        w_file.write(doc.getvalue())
    
    print(f"Report generated: {filename}")


def generate_professor_report(p_id: int, filename="Utils/reports/professor_report.html") -> None:
    
    professor = view_single_professor(p_id)
    courses = view_professor_classes(p_id)

    course_list = []
    for index, row in enumerate(courses):
        course = view_students_enrolled_in_class(row.c_id)
        course_list.append(course)

    doc, tag, text = Doc().tagtext()

    doc.asis('<!DOCTYPE html>')
    with tag('html'):
        with tag('head'):
            with tag('title'):
                text('Professor Report')
        
        with tag('body'):
            with tag('h1'):
                text(f"{professor.f_name.capitalize()}'s Summary Report")
            
            with tag('p'):
                with tag('b'):
                    text('First name: ')
                text(professor.f_name.capitalize())

            with tag('p'):
                with tag('b'):
                    text('Last name: ')
                text(professor.l_name.capitalize())

            with tag('p'):
                with tag('b'):
                    text('Email: ')
                text(professor.email)

            with tag('p'):
                with tag('b'):
                    text('Department: ')
                text(professor.department.capitalize())
            
            with tag('h2'):
                text('Classes:')

            with tag('ul'):
                for index, course_info in enumerate(courses):
                    students_in_class = course_list[index]

                    with tag('li'):
                        with tag('b'):
                            text('Class name: ')
                        text(course_info.c_name.capitalize())
                        doc.stag('br')
                        doc.stag('br')

                        with tag('b'):
                            text('Course code: ')
                        text(str(course_info.course_code))
                        doc.stag('br')
                        doc.stag('br')

                        with tag('b'):
                            text('Students: ')
                        
                        if students_in_class:
                            student_names = [f"{s.f_name.capitalize()} {s.l_name.capitalize()}" for s in students_in_class]
                            text(", ".join(student_names))
                        else:
                            text("No students currently enrolled.")

                    doc.stag('br')
                    doc.stag('br')


    with open(filename, "w") as w_file:
        w_file.write(doc.getvalue())
    
    print(f"Report generated: {filename}")

