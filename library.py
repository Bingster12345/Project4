class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        return f"'{self.title}' by {self.author}"


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available:
            self.borrowed_books.append(book)
            book.is_available = False
            return True
        return False

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_available = True
            return True
        return False

    def __str__(self):
        return f"{self.name} (ID: {self.user_id})"


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title, author):
        self.books = [book for book in self.books if book.title != title or book.author != author]

    def register_user(self, user):
        self.users.append(user)

    def find_book(self, title, author):
        return next((book for book in self.books if book.title == title and book.author == author), None)

    def list_available_books(self):
        return [book for book in self.books if book.is_available]
