#Constructor - Special method automatically called when an object is created and is used to initialize the attributes of object
#Deconstructor - It is a special method called del

class Myclass:
    def __init__(self):
        print("Constructor")
    
    def __del__(self):
        print("Deconstructor")

obj = Myclass()
del obj

#types of constructors:
#1) Constructor without arguments - define constructor method without any argument
class MyClass:
    def __init__(self):
        self.data = 10
print(MyClass().data)

#2) Constructor with arguments - define constructor that takes arguments to initialize
class Person:
    def __init__(self, age):
        self.data = age
p1= Person(45)
print(p1.data)

#3) Constructor with default arguments - constructors are defined using init method and automatically called when an object is created
class Person:
    def __init__(self, age="Unknown"):
        self.data = age
p1=Person()
p2=Person(26)
print(p1.data)
print(p2.data)