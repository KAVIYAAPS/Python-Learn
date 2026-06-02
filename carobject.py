class car:
    def __init__(self,name,brand):
        self.name=name
        self.brand=brand
    def display(self):
        print("Name:",self.name)
        print("Brand:",self.brand)

cars=car("Exter","Hyundai")
cars.display()