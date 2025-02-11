# Student Management System with Student Details

#Print("Welcome to the Student Management System")

students = {}
while True:
    print ('''Choose an option: 
    1. Add a Student
    2. Remove a Student
    3. View one Student
    4. View All Students
    5. Exit ''')




    choice = input("Choose an option from 1 - 5: ")

    if choice == "1":
        #add a student
        student_id = input("enter student ID: ")
        name = input("enter name: ")
        age = int(input("enter age: "))
        grade = input("enter grade: ")
        course = input("enter course: ")

        students[student_id] = {'name': name, 'age':age, 'grade':grade, 'course':course} #creating a sub dict(students_id) as user input, inside the master dict(students) and assigning key-value pairs to it

        print(f"{name} has been added to the system")
        print(students)

    #remove student
    elif choice == "2":
        student_id = input("enter student to remove: ")
        if student_id in students:#if this student id is in our students master dictionary,
            del students[student_id] # delete that student id and it's associated content from master dictionary (students)
            print(f"{name} has been removed from the system")
        else:
            print("student not found")

    #view one student
    elif choice == "3":
        student_id = input("enter student ID to view: ")
        if student_id in students: 
            particular_student_details = students[student_id] # get that particular students detail and store in this variable
            print(f"Student ID: {student_id}") #prints the student ID
            print(f"Name: {particular_student_details['name']}") #prints that particular student's name
            print(f"Age: {particular_student_details['age']}")
            print(f"Grade: {particular_student_details['grade']}")
            print(f"Course: {particular_student_details['course']}")
        else:
            print("Student not found")

    #view all students      
    elif choice == "4":
        if students:
            print("Student list: ")
            print(students)
        else:
                print("No students in the system")
    elif choice == "5":
        print("Goodbye")
        break

    else:
        print("Please enter a number between 1 and 5")

            
            





