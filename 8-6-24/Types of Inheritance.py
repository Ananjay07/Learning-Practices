#Types of Inheritance
#1) Single Inheritance enables a derived class to inherit properties from a single parent class, thus enabling code reusability and the addition of new features to existing code.
class Animal:
    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):                  #Class Dog inherits the class Animal
    def make_sound(self):
        print("WOOF!")
animal = Animal()
animal.make_sound()
dog = Dog()
dog.make_sound()

#2) Multiple inheritance allows a subclass to inherit from multiple parent classes.
class Trait1:
  def hunt(self):
    print("Generic hunting behavior")

class Trait2:
  def have_fur(self):
    print("Has fur")

class Wolf(Trait1, Trait2):  # Wolf inherits from both Trait1 and Trait2
  def make_sound(self):
    print("Howl!")

wolf = Wolf()
wolf.hunt()
wolf.have_fur()
wolf.make_sound()

#3) Multilevel Inheritance features of the base class and the derived class are further inherited into the new derived class
class Animal:
  def make_sound(self):
    print("Generic animal sound")

class Mammal(Animal):  # Mammal inherits from Animal
  def give_birth(self):
    print("Giving live birth")

class Dog(Mammal):  # Dog inherits from Mammal which inherits from Animal
  def make_sound(self):
    print("Woof!")

dog = Dog()
dog.make_sound()
dog.give_birth()

#4) Hierarchical Innheritance Multiple subclasses inherit from a single class. 
#More than one derived class are created from a single base
class Animal:
  def make_sound(self):
    print("Generic animal sound")

class Dog(Animal):  #Dog inherits from Animal
  def make_sound(self):
    print("Woof!")

class Cat(Animal):  #Cat inherits from Animal
  def make_sound(self):
    print("Meow!")
dog = Dog()
cat = Cat()
dog.make_sound()
cat.make_sound()

#5) Hybrid Inheritance has multiple types of inheritance
class Bird:
  def __init__(self):
    self.wings = 2

  def fly(self):
    print("Soaring through the sky!")

class LandAnimal:
  def __init__(self):
    self.legs = 4

  def roar(self):
    print("Loud animal roar!")

class Griffin(Bird, LandAnimal):  # Hybrid inheritance (inherits from both Bird and LandAnimal)
  def make_sound(self):
    print("A mighty screech combined with a powerful roar!")

griffin = Griffin()
griffin.make_sound()