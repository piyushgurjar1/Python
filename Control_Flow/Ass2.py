books = []

def add_book():
    book = input("Enter the book title to add: ")
    books.append(book)

def remove_book():
    book = input("Enter the book title to remove: ")
    if book in books:
        books.remove(book)
        print(f'"{book}" has been removed from the library.')
    else:
        print(f'"{book}" is not in the library.')

def search_book():
    book = input("Enter the book title to search: ")
    if book in books:
        print(f'"{book}" is in the library.')
    else:
        print(f'"{book}" is not in the library.')

def list_books():
    if books:
        print("Books in the library:")
        for book in books:
            print(f"{book}",)

print('''Library Menu:
1. Add a book
2. Remove a book
3. Search for a book
4. List all books''')


while True:
    choice = input("Choose an option (1-4): ") 

    if choice == "1":
        add_book()  
    elif choice == "2":
        remove_book() 
    elif choice == "3":
        search_book()  
    elif choice == "4":
        list_books()  
    else:
        print("Invalid option!")
        break