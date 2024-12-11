from library import Book, Student, Teacher, Library

def main():
    library = Library()

    # Add books to the library
    library.add_book(Book("1984", "George Orwell"))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))

    # Register users
    student = Student("Alice", 1)
    teacher = Teacher("Bob", 2)
    library.register_user(student)
    library.register_user(teacher)

    # Borrow books
    book1 = library.find_book("1984", "George Orwell")
    book2 = library.find_book("To Kill a Mockingbird", "Harper Lee")

    print(f"\nBorrowing as a Student:")
    if book1 and student.borrow_book(book1):
        print(f"{student.name} successfully borrowed {book1}")
    if book2 and student.borrow_book(book2):  # Should fail due to borrowing limit
        print(f"{student.name} successfully borrowed {book2}")

    print(f"\nBorrowing as a Teacher:")
    if book2 and teacher.borrow_book(book2):
        print(f"{teacher.name} successfully borrowed {book2}")

    # List available books
    print("\nAvailable books:")
    for book in library.list_available_books():
        print(book)

    # Return books
    print(f"\nReturning books:")
    if student.return_book(book1):
        print(f"{student.name} returned {book1}")
    if teacher.return_book(book2):
        print(f"{teacher.name} returned {book2}")

    # List available books again
    print("\nAvailable books after return:")
    for book in library.list_available_books():
        print(book)


if __name__ == "__main__":
    main()
