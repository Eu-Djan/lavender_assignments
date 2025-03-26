import psycopg2   #import package

#connect to Database

try:
    connection = psycopg2.connect(dbname = "employee_db", user = "postgres", password = "eugzz", host = "127.0.0.1", port = "5432")

    cursor = connection.cursor()  
    print("Connection successful")

except:
    print("Something went wrong")

#CREATING EMPLOYEE TABLE

cursor.execute (""" CREATE TABLE IF NOT EXISTS employees (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(50) NOT NULL,
                        age INTEGER NOT NULL,
                        department VARCHAR(50) NOT NULL
                        );               
                """)

#cursor.execute("INSERT INTO employees (name, age, department) VALUES (%s, %s, %s) ", ('Harry K', 45, 'DTT') )

#INSERTING NEW EMPLOYEE

def add_employee(name, age, department):
    
    cursor.execute(" SELECT name, age, department FROM employees")
    all_employees = cursor.fetchall()
    for employee in all_employees:
        if name in employee and age in employee and department in employee:
            print("This employee already exists")
            return
        else:
            cursor.execute(" INSERT INTO employees (name, age, department) VALUES (%s, %s, %s)" , (name, age, department) )
            connection.commit()
            print(f"Employee with name {name} added successfully")

#add_employee('Eon', 23, 'NOC')

#RETRIEVE AND DISPLAY ALL EMPLOYEES

def view_employees():
    cursor.execute("SELECT * FROM employees")
    all_employees = cursor.fetchall()

    print(all_employees)

#view_employees()

#UPDATE AN EMPLOYEE'S INFO

def update_employee(id, name, age, department):
    cursor.execute("UPDATE employees SET name = %s, age = %s, department = %s WHERE id = %s ", (name, age, department, id) )

    connection.commit()
    print(f"Employee {name} with id {id} has been updated")

#update_employee(3, 'Eon', 27, 'NOC')

#DELETE AN EMPLOYEE

def delete_employee(id, name):
    cursor.execute(" SELECT * FROM employees WHERE id = %s and name = %s", (id,name))
    employee = cursor.fetchone()

    if employee:
        cursor.execute(" DELETE FROM employees WHERE id = %s and name = %s", (id,name))
        connection.commit()
        print(f"Employee with name {name} and id '{id}' removed successsfully")
    else:
        print(f"Employee with name {name} id '{id}' not found ")

#delete_employee(4, 'Eon')


def main_menu():

    
        while True:

            print ('''Choose an option: 
            1. Add Employee
            2. View Employees
            3. Update Employee 
            4. Delete Employee
            5. Exit ''')
                    
            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter employee name: ")
                age = int(input("Enter employee age: "))
                department = input("Enter employee department: ")
                add_employee(name, age, department)

            elif choice == "2":
                view_employees()

            elif choice == "3":
                id = input("Enter employee id to update: ")
                name = input("Enter employee name: ")
                age = int(input("Enter employee age: "))
                department = input("Enter employee department: ")
                update_employee(id, name, age, department)

            elif choice == "4":
                id = input("Enter employee id to delete: ")
                name = input("Enter employee name: ")
                delete_employee(id,name)

            elif choice == "5":
                print("goodbye")
                break
                
            else:
                print("Invalid choice, choose a number from 1 - 5 ")

        
main_menu()



#connection.commit()  # to persist the changes to pg Admin

cursor.close() #close the cursor at the end of all operations

connection.close()
