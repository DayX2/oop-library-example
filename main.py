class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class User(Person):
    def __init__(self, name, age, user_id):
        super().__init__(name, age)
        self.user_id = user_id

class Librarian(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def __str__(self):
        return f"'{self.title}' by {self.author}"
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)

user = User("Alice", 20, 4201)
print(user.name, user.age, user.user_id)

librarian = Librarian("Bob", 40, 10749386)
print(librarian.name, librarian.age, librarian.employee_id)

book1 = Book("1984", "George Orwell")
book2 = Book("Pride and Prejudice", "Jane Austen")

library = Library()
library.add_book(book1)
library.add_book(book2)

library.list_books()