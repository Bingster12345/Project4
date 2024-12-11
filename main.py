from library import Book, User, Library

def main():
    library = Library()

    # Add books to the library
    library.add_book(Book("1984", "George Orwell"))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))

    # Register users
    user1 = User("Alice", 1)
    user2 = User("Bob", 2)
    library.register_user(user1)
    library.register_user(user2)

    # Borrow books
    book_to_borrow = library.find_book("1984", "George Orwell")
    if book_to_borrow and user1.borrow_book(book_to_borrow):
        print(f"{user1.name} successfully borrowed {book_to_borrow}")

    # List available books
    print("\nAvailable books:")
    for book in library.list_available_books():
        print(book)

    # Return books
    if user1.return_book(book_to_borrow):
        print(f"\n{user1.name} returned {book_to_borrow}")

    # List available books again
    print("\nAvailable books after return:")
    for book in library.list_available_books():
        print(book)


if __name__ == "__main__":
    main()
