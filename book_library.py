#Book Library Project
book_library = ["LOTR"]
print(book_library)
print ('''Choose an option: 
1. Add a Book
2. Remove a Book
3. View All Books
4. Exit ''')

while True:
    choice = input("Enter choice: ")
#add a book
    if choice == "1":
        book =input("Enter book Title: ").split(",")
        if book in book_library: #checks if book already exists
            print(f"{book} already exists")
        else: 
            book_library.extend(book)
            print(f"{book} has been added")
            print(f"Your updated book library: ", book_library)
#Remove a  book
    elif choice == "2":
        book = input("Enter book title to remove: ")
        if book in book_library: #checks whether boook exists in the library
            book_library.remove(book)
            print(f"{book} has been removed")
        else:
            print("Book not found")
#View all Books
    elif choice == "3":
        print("Books in the library: ")
        if book_library:
            for book in book_library: #Iterates through the book library and print out all books present if any
                print(f"{book}")
        else:
            print("There are no books in the library")
#Exit
    elif choice == "4":
        print("Goodbye")
        break
    else:
        print("You must enter a choice from 1 - 4 ")
    


