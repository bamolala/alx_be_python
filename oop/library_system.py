# library_system.py

class Book:
    def __init__(self, title, author):
        """Base book class."""
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """EBook inherits from Book and adds file_size."""
        super().__init__(title, author)   # call base class constructor
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """PrintBook inherits from Book and adds page_count."""
        super().__init__(title, author)   # call base class constructor
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """Library uses composition to store multiple book objects."""
        self.books = []

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook instance."""
        self.books.append(book)

    def list_books(self):
        """Print details of every book in the library."""
        for book in self.books:
            print(book)   # uses each class's __str__ method
