from funciones import (
    add_book,
    add_history,
    search_book,
    list_books,
)

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
            add_book()

        elif choice == 2:
            add_history()

        elif choice == 3:
            search_book()

        elif choice == 4:
            list_books()

        elif choice == 5:
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")

    except ValueError as e:
        print(f"Error: {e}")
        
    print("\n"*10)