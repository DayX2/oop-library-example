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


user = User("Alice", 20, 4201)
print(user.name, user.age, user.user_id)

librarian = Librarian("Bob", 40, 10749386)
print(librarian.name, librarian.age, librarian.employee_id)



