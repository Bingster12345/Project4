class Book:
    def __init__(self, title, author):
        self._title = title  # Protected attribute
        self._author = author
        self._is_available = True

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def is_available(self):
        return self._is_available

    @is_available.setter
    def is_available(self, value):
        self._is_available = value

    def __str__(self):
        return f"'{self._title}' by {self._author}"


class User:
    def __init__(self, name, user_id):
        self._name = name
        self._user_id = user_id
        self._borrowed_books = []

    @property
    def name(self):
        return self._name

    @property
    def user_id(self):
        return self._user_id

    @property
    def borrowed_books(self):
        return self._borrowed_books

    def borrow_book(self, book):
        if book.is_available:
            self._borrowed_books.append(book)
            book.is_available = False
            return True
        return False

    def return_book(self, book):
        if book in self._borrowed_books:
            self._borrowed_books.remove(book)
            book.is_available = True
            return True
        return False

    def __str__(self):
        return f"{self._name} (ID: {self._user_id})"


class Student(User):
    def __init__(self, name, user_id):
        super().__init__(name, user_id)
        self.borrow_limit = 2

    def borrow_book(self, book):
        if len(self.borrowed_books) < self.borrow_limit:
            return super().borrow_book(book)
        else:
            print(f"{self.name} has reached the borrowing limit of {self.borrow_limit} books.")
            return False


class Teacher(User):
    def __init__(self, name, user_id):
        super().__init__(name, user_id)
        self.borrow_limit = 5

    def borrow_book(self, book):
        if len(self.borrowed_books) < self.borrow_limit:
            return super().borrow_book(book)
        else:
            print(f"{self.name} has reached the borrowing limit of {self.borrow_limit} books.")
            return False


class Library:
    def __init__(self):
        self._books = []
        self._users = []

    def add_book(self, book):
        self._books.append(book)

    def remove_book(self, title, author):
        self._books = [book for book in self._books if book.title != title or book.author != author]

    def register_user(self, user):
        self._users.append(user)

    def find_book(self, title, author):
        return next((book for book in self._books if book.title == title and book.author == author), None)

    def list_available_books(self):
        return [book for book in self._books if book.is_available]
