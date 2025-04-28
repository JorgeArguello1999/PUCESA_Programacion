from libro import Book, History

database = []

def add_book() -> None:
    "Interface to add a new book"
    try:
        print()
        book = Book(
            title=input("Enter the book title: "),
            author=input("Enter the author: "),
            isbn=input("Enter the ISBN: "),
            genero=input("Enter the gender: ")
        )
        print(f"\nBook added: {book}")
        database.append(book)

    except ValueError as e:
        print(f"Error: {e}")

def add_history() -> None:  
    "Interface to add a new history entry"
    try:
        print()
        title = input("Enter the book title: ")
        for i in database:
            if i.title == title:
                i.add_history(History(
                    action=bool(int(input("Enter the action (1 for Active, 0 for Inactive): "))),
                    date=input("Enter the date (YYYY-MM-DD): ")
                ).get())
                print(f"\nHistory added to book: \n{i.get()}")
            else:
                print("\nBook not found.")
                break

    except Exception as e:
        print(f"Error: {e}")
        return False

def search_book() -> None:
    "Interface to search for a book"
    search_term = input("Enter the search term (title): ")
    print(f"Searching for books with term: {search_term}\n")
    for i in database:
        if search_term.lower() in i.title.lower():
            book = i
            print(f"\nBook found: {book}")
            for history in book.get()["history"]:
                print(history)
            break

def list_books() -> None:
    "Interface to list all books"
    print("Listing all books:")
    print()
    for i in database:
        print(f"{i}")