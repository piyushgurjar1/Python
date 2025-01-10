class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', year={self.year})"

    def __lt__(self, other):
        if isinstance(other, Book):
            return self.title < other.title
        return False

    def __lt__(self, other):
        if isinstance(other, Book):
            return self.author < other.author
        return False

    def __lt__(self, other):
        if isinstance(other, Book):
            return self.year < other.year
        return False

book1 = Book("To Journey to Consultadd", "Me", 2024)
book2 = Book("Harry Potter", "J.K", 1900)


books = [book1, book2]

print("Books sorted by title:", sorted(books))
print("Books sorted by author:", sorted(books, key=lambda x: x.author)) 
print("Books sorted by year:", sorted(books, key=lambda x: x.year))
