#Pass objects as arguments
class math:
    def __init__(self, value):
        self.data = value
    
    def update(self, other):
        self.data += other.data

num1=math(5)
print(num1.data)
num2=math(10)
num1.update(num2)
print(num1.data)

#Object as a return type - create and return objects to encapsulate data within objects
class math:
    def __init__(self, value):
        self.data = value
    def increment(self):
        self.data +=1
        return self    #self.data is returned after incrementing
num1=math(10)
print(num1.data)
num2=num1.increment()
print(num2.data)

#Method overloading - allows to have multiple methods with same name but different parameter lsits
class person:
    def my_method(self, name, age="Unkown"):
        print(f"His name is {name} and his age is {age}")
p1=person()
p1.my_method("Max",26)
p1.my_method("Lewis")