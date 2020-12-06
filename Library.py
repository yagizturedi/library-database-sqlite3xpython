from LibraryDatabase import Classes

print("""***************************
Welcome to Library Database
***************************

Operations

1. Show Books
2. Query Book
3. Add Book
4. Remove Book
5. Update Edition

To exit press "q"

""")

library = Classes.Library()


while True:

    operation = input("Enter the number of the operation: ")

    if operation == "q":
        print("Thank you for visiting the library.")
        library.disconnect()
        break

    elif operation == "1":
        print("Books in the library\n")
        print( "\n" )
        library.showBooks()

    elif operation == "2":
        book_name = input("Please enter the name of the book: ")
        print( "\n" )
        library.queryBook(book_name)

    elif operation == "3":
        book_name = input("Please enter the name of the book: ")
        author = input( "Please enter the author of the book: " )
        publisher = input( "Please enter the publisher of the book: " )
        genre = input( "Please enter the genre of the book: " )
        edition = int(input( "Please enter the edition of the book: " ))
        print( "\n" )

        book = Classes.Book( book_name, author, publisher, genre, edition )
        library.addBook(book)

    elif operation == "4":
        book_name = input("Please enter the name of the book: ")

        try:
            library.removeBook(book_name)
            print("Books are successfully removed.")
        except:
            print("An error has occured.")

    elif operation == "5":
        book_name = input( "Please enter the name of the book: " )

        try:
            library.updateEdition( book_name )
            print("Edition has successfully been updated.")
        except 1:
            print("An error has occured.")

