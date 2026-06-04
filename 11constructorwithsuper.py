class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll

    def display(self):
        print(self.name)
        print(self.roll)

s = Student("Kavya", 101)
s.display()