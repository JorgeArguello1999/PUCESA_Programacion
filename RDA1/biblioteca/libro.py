from datetime import datetime

class History:
    def __init__(self, action:bool, date:str=None) -> None:
        """
        Initialize a History object with date and action.
        :param date: Date of the action or by default the current date
        :param action: Active(1) or Inactive action
        """
        if len(date) > 10:
            raise ValueError("Date format is incorrect. Use YYYY-MM-DD.")
            
        try:
            self.date = str(date) or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.action = bool(action)
        except ValueError as e:
            print(f"Error initializing History: {e}")
            raise

    def get(self) -> dict:
        """
        Return a dictionary representation of the History object.
        :return: Dictionary representation of the history
        """
        return {
            "date": self.date,
            "action": self.action
        }
    
    def __repr__(self):
        """
        Return a string representation of the History object for debugging.
        :return: String representation of the history
        """
        return f"History(date={self.date}, action={self.action})"

class Book:
    history = []
    title = ""

    def __init__(self, title:str, author:str, isbn:str, genero:str) -> None:
        """
        Initialize a Book object with title, author, isbn, and genero.
        :param title: Title of the book
        :param author: Author of the book
        :param isbn: ISBN of the book
        :param genero: Genre of the book
        """
        if not all([title, author, isbn, genero]):
            raise ValueError("All fields are required.")
        
        try: 
            self.title = str(title)
            self.author = str(author)
            self.isbn = str(isbn)
            self.genero = str(genero)
            self.history = []

        except ValueError as e:
            print(f"Error initializing Book: {e}")
            raise
    
    def add_history(self, history:History) -> bool:
        """
        Add a history entry to the Book object.
        :param history: History entry to be added
        """
        try:
            self.history.append(history)
            return True

        except ValueError as e:
            print(f"Error adding history: {e}")
            return False

    def get(self) -> dict:
        """
        Return a dictionary representation of the Book object.
        :return: Dictionary representation of the book
        """
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "genero": self.genero,
            "history": self.history
        }
    
    def __str__(self) -> str:
        """
        Return a string representation of the Book object.
        :return: String representation of the book
        """
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Genre: {self.genero}"

    def __repr__(self) -> str:
        """
        Return a string representation of the Book object for debugging.
        :return: String representation of the book
        """
        return f"Book({self.title}, {self.author}, {self.isbn}, {self.genero})"