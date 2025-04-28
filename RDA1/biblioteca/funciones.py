from libro import Book, History

def add_book() -> None:
    "Interface to add a new book"
    try:
        title = input("Enter the book title: ")
        author = input("Enter the author: ")
        isbn = input("Enter the ISBN: ")
        genero = input("Enter the gender: ")
        book = Book(title, author, isbn, genero)
        print(f"Book added: {book.get()}")

    except ValueError as e:
        print(f"Error: {e}")

def add_history() -> None:  # Work here
    "Interface to add a new history entry"
    date = input("Enter the date (YYYY-MM-DD): ")
    action = input("Enter the action (1 for Active, 0 for Inactive): ")
    history = History(date, action)
    print(f"History added: {history.get()}")

def search_book() -> None:
    "Interface to search for a book"
    search_term = input("Enter the search term (title/author): ")
    print(f"Searching for books with term: {search_term}")

def list_books() -> None:
    pass