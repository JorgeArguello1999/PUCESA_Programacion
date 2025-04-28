separator = "-"*33

menu = f"""
{separator}
Welcome to the Book Management System
{separator}
1. Add a new book
2. Add a new history entry
3. Search for a book
4. List all books
5. Exit
{separator}
Please choose an option (1-5):"""

while __name__ == "__main__":
    try:
        choice = int(input(menu))
        if choice == 1:
            title = input("Enter the book title: ")
            author = input("Enter the author: ")
            isbn = input("Enter the ISBN: ")
            genero = input("Enter the gender: ")
            # book = Book(title, author, isbn, genero)
            # print(f"Book added: {book.get()}")

        elif choice == 2:
            date = input("Enter the date (YYYY-MM-DD): ")
            action = input("Enter the action (1 for Active, 0 for Inactive): ")
            # history = History(date, action)
            # print(f"History added: {history.get()}")

        elif choice == 3:
            search_term = input("Enter the search term (title/author): ")
            # Implement search logic here

        elif choice == 4:
            pass
            # Implement list all books logic here

        elif choice == 5:
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")
    except ValueError as e:
        print(f"Error: {e}")