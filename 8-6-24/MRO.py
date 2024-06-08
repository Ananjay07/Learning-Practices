#Method Resolution Order - is a set of rules that define the order in which Python searches for methods when you call them on an object of a class that inherits from multiple parent classes.
#When two parent classes have a method with the same name and call that method on an object of the child class, MRO tells which method definition Python uses to resolve the call
#This ensures predictable behavior in the code
class Vehicle:
  def move(self):
    print("Normal vehicle movement")

class ElectricCar(Vehicle):  #Electric car inherits from Vehicle
  def move(self):
    print("Electric car silently moving")

class LuxuryCar(Vehicle):  #Luxury car inherits from Vehicle
  def move(self):
    print("Luxury car cruising smoothly")

class ElectricLuxuryCar(ElectricCar, LuxuryCar):  #Above two classes are combined in this child class (multiple inheritance)
  pass

print(ElectricLuxuryCar.__mro__)            #MRO is printed

tesla_model_s = ElectricLuxuryCar()
tesla_model_s.move()