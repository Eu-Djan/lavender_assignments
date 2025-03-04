# Library management System
#  Design and  implement a Python program to manage a library's collection of books/
# The program should be able to allow user to add a book, remove books, search for a book by title and author
# and display all the books in the library.


# LIBRARY MANAGEMENT SYSTEM
# 1. Add a Book
# 2. Remove a Book
# 3. Search for a Book
# 4. Display All books
# 5. Exit program

class Library:
    def __init__(self):
        self.books = [] 

    def add_book(self, title):
        self.books.append(title)
        print(f" {title} has been added to library")

    def remove_book(self, title):
        if title in self.books:
            self.books.remove(title)
            print(f"{title} has been removed")
        else:
            print(f"{title} not found in library")

    def search_book(self, title):
        if title in self.books:
            print(f"{title} is in the library")
        else:
            print(f"{title} is not in the library")
    
    def display_all_books(self):
        if self.books:
            print("These are the available books in the library:")
            for book in self.books:
                print(book)
        else:
                print("There are no books in the library")

def main_menu():

    library = Library()

    while True:

            print ('''Choose an option: 
            1. Add a Book
            2. Remove a Book
            3. Search for a Book 
            4. Display All Books
            5. Exit ''')
                    
            choice = input("Enter your choice: ")

            if choice == "1":
                book_title = input("Enter book to add: ")
                library.add_book(book_title)
            elif choice == "2":
                book_title = input("Enter book to remove: ")
                library.remove_book(book_title)
            elif choice == "3":
                book_title = input("Enter Book title: ")
                library.search_book(book_title)
            elif choice == "4":
                library.display_all_books()
            elif choice == "5":
                print("Goodbye")
                break
            else:
                print("Invalid choice. Choose a number from 1 - 5")

main_menu()
        
