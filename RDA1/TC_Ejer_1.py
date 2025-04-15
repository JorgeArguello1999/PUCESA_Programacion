# Book Class
class Book:
    def __init__(self, title, author, year, price):
        self.title = title
        self.author = author
        self.year = year
        self.price = price
    
    def description(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}, Price: ${self.price}"
    
    def __str__(self):
        return self.description()

# Use the Book class to create a list of books
book1 = Book("1984", "George Orwell", 1949, 15.99)
book2 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 1997, 20.99)

# View the details of the books
print(book1)
print(book2)

print()
print()

# Class student
class Student:
    def __init__(self, name, career, final_degree):
        self.name = name
        self.career = career
        self.final_degree = final_degree
    
    def description(self):
        return f"Name: {self.name}, Career: {self.career}, Final Degree: {self.final_degree}"
    
    def aprove(self):
        return True if self.final_degree >= 70 else False
    
    def __str__(self):
        return f"Name: {self.name}, Aprove: {self.aprove()}"

# Use the Student class to create a list of students
student1 = Student("Alice", "Computer Science", 85)
student2 = Student("Bob", "Mathematics", 65)

# View the details of the students
print(student1)
print(student2)

# Know if the students passed
print(student1.description(), student1.aprove())
print(student2.description(), student2.aprove())

print()
print()

# Class Vehicle
class Vehicle:
    def __init__(self, model, speed:float=0.0):
        self.model = model
        self.speed = speed
    
    def move(self):
        return f"The vehicle {self.model} is moving at {self.speed} km/h."
    
class Auto(Vehicle):
    def move(self):
        return f"The auto {self.model} is moving at {self.speed} km/h."

# Use the Vehicle class to create a list of vehicles
vehicle1 = Vehicle("Airplane", 800)
vehicle2 = Vehicle("Train", 200)

# Auto
auto1 = Auto("Toyota", 120)
auto2 = Auto("Mercedes", 150)

# View the details of the vehicles
print(vehicle1.move())
print(vehicle2.move())
print()

# View the details of the autos
print(auto1.move())
print(auto2.move())

print()
print()

# Class Bird
class Bird:
    def sound(self):
        return "Chirp"

# Class Cat
class Cat:
    def sound(self):
        return "Meow"

# Polymorphism
def make_sound(animal):
    print(animal.sound())

# Use the Bird and Cat classes
bird = Bird()
cat = Cat()

# View the sounds of the animals
make_sound(bird)
make_sound(cat)
