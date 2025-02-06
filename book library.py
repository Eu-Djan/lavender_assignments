#Book Library Project


book_library = []
print(book_library)
print ('''Choose an option: 
1. Add a Book
2. Remove a Book
3. View All Books
4. Exit ''')

choice = input("Enter choice: ")

# Add a Book
if choice == "1":
  book = input("Enter book title: ")
  if book in book_library: #checks if book already exists the book library list
      print(f"{book} already exists")
  else:
    book_library.append(book) #adds or appends book to the book_library list
    print(f"{book} has been added to the library" )
    
#Remove a book
elif choice == "2":
    book = input("Enter book title to remove: ")
    if book in book_library: #checks whether book exists in the book library
        book_library.remove(book) #removes book from book library
        print(f"{book} has been removed")
    else:
        print("Book not found")
      
#View All Books      
elif choice == "3":
    print("Books in the library: ")
    if book_library: #checks if there are items in the book_library
        for book in book_library:
            print(f"{book}") #print each item(book) found in the book_library
    else:
        print("There are no books in the library")
      
#Exit
elif choice == "4":
    print("Goodbye")
    

else:
    print("You must enter a choice from 1-4: ")



