#Inheritance is a way to create new classes ( child classes) that inherit properties and methods from existing classes (parent class)
#the child class acquires the properties and can access all the data members and functions defined in the parent class
#syntax:
class ParentClass:
    def parent(self):           #These are parent class attributes and methods
       return

class ChildClass(ParentClass):
    def child(self):            #These are child class attributes and methods (can inherit from parent)
       return

#example:
class Animal:               #parent class is created
  def __init__(self, name):
    self.name = name

  def make_sound(self):
    print("General animal sound")

class Dog(Animal):          #child class is created which inherits properties from parent class
  def make_sound(self):
    print(f"{self.name} barks!")

animal = Animal("General")
animal.make_sound()         
dog = Dog("Ludo")
dog.make_sound()