# Create a program that manages student records, including their names, ages, and grades. The program should allow you to:


# Add new students.
# Update existing student records.
# Calculate and display the average grade of all students.
# Display all student records.

students = {}
scores = [] #scores list will be used later to calculate average scores and average grade


choice = input("Choose an option from 1 - 5: ")

#add student
def add_student():
    student_id = input("enter student ID: ")
    name = input("enter name: ")
    age = int(input("enter age: "))
    score = int(input("enter raw score: "))
    grade = input("enter grade: ")


    students[student_id] = {'name': name, 'age':age, 'score':score, 'grade':grade} #creating a sub dict(students_id) as user input, inside the master dict(students) and assigning key-value pairs to it

    print(f"{name} has been added to the system")
    print(students)

#update
def update_student():
    student_id = input("enter username to update: ")
    if student_id in students:
        print(student_id)
        print(students[student_id])
        make_changes = input("do you want to make any changes?: ").lower()
        if make_changes == "yes":
            add_student()
        else:
            print(f"students list: {students}")
    else:
        print("username not found")  


#calculate and display average grade of all students
def average_grade():
    for student_id in students:
        scores.append(students[student_id]['score']) #appending the extracted score to an empty list called scores = []. This would help us get elements in a list format to help with calculating the average score
        print (scores)
        #calculate the average score using items in the  scores list. We make use of the sum() function and len() function 
    average_score = sum(scores) / len(scores)
    print(f"The average score is: {average_score}")

    grade = ""
    # we use control statements to determine the average grade using the result from the average score.
    if average_score >= 80:
        grade = "A"
        print(f"The average grade is {grade}")
    elif average_score >=70:
        grade = "B"
        print(f"The average grade is {grade}")
    else:
        print("The average grade is C and below")

def view_all_students():
    if students:
        print("Student list: ")
        print(students)
    else:
        print("No students in the system")
        
def exit():
    print("Goodbye")


def main_menu():
    while True:
        print ('''Choose an option: 
        1. Add a Student
        2. Update Student
        3. Display average Grade of students
        4. View All Students
        5. Exit ''')
    
        choice = input("Choose an option from 1 - 5: ")
    
        if choice == "1":
            add_student()
        elif choice == "2":
            update_student()
        elif choice == "3":
            average_grade()
        elif choice == "4":
            view_all_students()
        elif choice == "5":
            exit()
            break
        
        else:
            print("Please enter a number between 1 and 5")
    

main_menu()