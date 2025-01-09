def input_catalog():
    catalog = []
    n = int(input("Enter the number of books you want to add: "))
    while True:
        title = input("Enter the book title: ")    
        author = input("Enter the author: ")
        category = input("Enter the category: ")
        catalog.append({"title": title, "author": author, "category": category})
        print("Book added to catalog.")
        if len(catalog) == n:
            break
    return catalog

def search_by_title(catalog, title):
    results = []
    for book in catalog:
        if title.lower() == book["title"].lower():
            results.append(book)
    return results

def search_by_author(catalog, author):
    results = []
    for book in catalog:
        if author.lower() == book["author"].lower():
            results.append(book)
    return results

def search_by_category(catalog, category):
    results = []
    for book in catalog:
        if category.lower() == book["category"].lower():
            results.append(book)
    return results

def display_books(books):

    if books:
        for book in books:
            print(f"Title: {book['title']}, Author: {book['author']}, Category: {book['category']}")
    else:
        print("No books found.")

print("Welcome to the Library Catalog System")

library = input_catalog()

print('''Library Catalog Menu:
1. Search by Title
2. Search by Author
3. Search by Category
4. Exit''')

while True:
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        title = input("Enter the title to search for: ")
        books = search_by_title(library, title)
        display_books(books)

    elif choice == "2":
        author = input("Enter the author to search for: ")
        books = search_by_author(library, author)
        display_books(books)

    elif choice == "3":
        category = input("Enter the category to search for: ")
        books = search_by_category(library, category)
        display_books(books)

    else:
        print("Invalid option")
        break