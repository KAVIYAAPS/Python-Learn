class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display(self):
        print(self.name)
        print(self.age)
        print(self.subject)

t = Teacher("Kavya", 20, "Python")
t.display()