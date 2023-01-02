while(True):
    print("\n 1.  Student operations")
    print(" 2.  Course operations")
    print(" 3.  Batch operations")
    print(" 4.  Department operations")
    print(" 5.  Examination operations")
    print(" 0.  Stop")
    x = int(input("Enter your choice: "))
    if(x == 0):
        print("You have succesfully exited")
        break
    elif(x == 1):
        from student import *
        while(True):
            print("\n1. Create a student")
            print("2. Update a student's details")
            print("3. Remove a student")
            print("4. Generate report card of a student")
            print("0. Return to main menu")
            y = int(input("Enter your choice: "))
            if(y == 0):
                break
            elif(y == 1):
                student_id = input("Enter student ID: ")
                student_name = input("Enter student name: ")
                createStudent(student_id, student_name)
            elif(y == 2):
                ostudent_id = input("Enter old student ID: ")
                updateStudent(ostudent_id)
            elif(y == 3):
                student_id = input("Enter student ID: ")
                removeStudent(student_id)
            elif(y == 4):
                student_id = input("Enter student ID: ")
                reportCard(student_id)
            else:
                print("Invalid input. Try again.")  
    elif(x == 2):
        from course import *
        while(True):
            print("\n  1. Create a course")
            print("  2. View performance of students on course")
            print("  3. Show course statistics as histogram")
            print("  0. Return to main menu")
            y = int(input("Enter your choice: "))
            if(y == 0):
                break
            elif(y == 1):
                course_id = input("Enter course ID: ")
                course_name = input("Enter course name: ")
                createCourse(course_id, course_name)
            elif(y == 2):
                course_id = input("Enter course ID: ")
                checkPerformance(course_id)
            elif(y == 3):
                course_id = input("Enter course ID: ")
                courseStatistics(course_id)
            else:
                print("Invalid input. Try again.")
    elif(x == 3):
        from batch import *
        while(True):
            print("\n 1.Create a batch")
            print(" 2.View all students in a batch")
            print(" 3.Show all courses in a batch")
            print(" 4.View performance of all students in a batch")
            print(" 5.View pie chart of percentage all students in a batch")
            print(" 0.Return to main menu")
            y = int(input("Enter your choice: "))
            if(y == 0):
                break
            elif(y == 1):
                batch_name = input("Enter batch name: ")
                createBatch(batch_name)
            elif(y == 2):
                batch_id = input("Enter batch ID: ")
                viewStudents(batch_id)
            elif(y == 3):
                batch_id = input("Enter batch ID: ")
                viewCourses(batch_id)
            elif(y == 4):
                batch_id = input("Enter batch ID: ")
                viewPerformance(batch_id)
            elif(y == 5):
                batch_id = input("Enter batch ID: ")
                pieChart(batch_id)
            else:
                print("Invalid input. Try again.")
    elif(x == 4):
        from department import *
        while(True):
            print("\n  1.Create a department")
            print("  2.View all batches in a department")
            print("  3.View average performance of all batches in a department")
            print("  4.View line plot of department statistics")
            print("  0.Return to main menu")
            y = int(input("Enter your choice: "))
            if(y == 0):
                break
            elif(y == 1):
                department_id = input("Enter department ID: ")
                department_name = input("Enter department name: ")
                createDepartment(department_id, department_name)
            elif(y == 2):
                department_id = input("Enter department ID: ")
                viewBatches(department_id)
            elif(y == 3):
                department_id = input("Enter department ID: ")
                viewPerformanceD(department_id)
            elif(y == 4):
                department_id = input("Enter department ID: ")
                linePlot(department_id)
            else:
                print("Invalid input. Try again.")
    elif(x == 5):
        from examination import *
        while(True):
            print("\n  1.Enter marks of all students for an exam")
            print("  2.View performance of all students in an exam")
            print("  3.Show examination statistics as a scatter plot")
            print("  0.Return to main menu")
            y = int(input("Enter your choice: "))
            if(y == 0):
                break
            elif(y == 1):
                course_id = input("Enter course ID: ")
                enterMarks(course_id)
            elif(y == 2):
                course_id = input("Enter course ID: ")
                viewPerformanceE(course_id)
            elif(y == 3):
                scatterPlot()
            else:
                print("Invalid input. Try again.\n")
    else:
        print("Invalid input. Try again.\n")
