#Advanced Bank ATM System


PIN = "1234"
balance = 1000.00
amount = 0
transaction_history = []


print("Welcome to 123 Bank ATM ")


  
while True:
    pin_code = input("enter PIN: ") 

    if pin_code == PIN:
        break
    else:
        print("Incorrect PIN, try again. ")        

          
    
       
#check balance
def check_balance():
    print(f"Your current balance is : {balance}")

#Make Deposit
def make_deposit(balance, amount):
    
    amount = float(input("How much do you want to deposit: "))
    if amount > 0:
        balance = balance + amount
        print(f"You have deposited {amount}, and your new balance is: {balance}")
        transaction_history.append(f"Deposit of: {amount}")
    else:
        print("Please deposit an amount more than 0")


#Withdraw Money
def withdraw(balance, amount):
    
    amount = float(input("How much do you want to withdraw? "))
    if amount >= balance:
        print("Your balance is insufficient to make this withdrawal ")
    else:
        balance = balance - amount
        print(f"You have withdrawn {amount}, your new balance is {balance}")
        transaction_history.append(f"Withdrawal of: {amount}")

#Check Transaction History
def history():
    print("Transaction History: ")
    if transaction_history:
        for transaction in transaction_history:
            print(transaction)
    else:
        print("No transactions found")

#Exit 
def exit():
    confirm_exit = input("Are you sure you want to exit? ").lower()
    if confirm_exit == "yes":
        print("GOODBYE ")
    


def main_menu():

    
        while True:

            print ('''Choose an option: 
            1. Check current balance
            2. Make Deposit
            3. Withdraw Money 
            4. Check transaction history
            5. Exit ''')
                    
            choice = input("Enter your choice: ")

            if choice == "1":
                check_balance()
            elif choice == "2":
                make_deposit(balance, amount)
            elif choice == "3":
                withdraw(balance, amount)
            elif choice == "4":
                history()
            elif choice == "5":
                exit()
                break
                
            else:
                print("Invalid choice, choose a number from 1 - 5 ")

        
main_menu()






    













