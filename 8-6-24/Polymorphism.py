#Polymorphism is the ability of objects of different classes to respond to the same message (method call) in different ways
#Polymorphism provides a common interface (method) that different classes can implement in their own specialized ways
#Code becomes more flexible as you can treat objects of different classes similarly through the same interface
#example:
class Vehicle:                                  #parent class created
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def accelerate(self):
        print(f"The {self.make} {self.model} accelerates.")

class Car(Vehicle):                             #child class is created
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)           # Call parent constructor
        self.num_doors = num_doors
    def accelerate(self):
        print(f"The {self.make} {self.model} with {self.num_doors} doors speeds up.")

class ElectricCar(Car):                         #Another child class is created within the class "Car"
    def __init__(self, make, model, num_doors, battery_range):
        super().__init__(make, model, num_doors)
        self.battery_range = battery_range
    def accelerate(self):
        print(f"The electric {self.make} {self.model} with {self.num_doors} doors zooms ahead silently.")

def go_for_a_drive(vehicle):                    #Here this is the polymorphic call which can be used by all types of cars
    vehicle.accelerate()

car = Car("Ford", "Everest", 4)
electric_car = ElectricCar("Tesla", "Model S", 4, 400)

go_for_a_drive(car)
go_for_a_drive(electric_car)                    #Polymorphism is used to perform the accelerate function depending on the inputs given and type of car