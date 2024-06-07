#_init_ method - used to initialize the object's attributes
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = person("Max Verstappen", 26)
p2 = person("Lewis Hamilton", 39)
print(p1.name)
print(p2.age)

#__str__ method - used to define string representation of object
#functions print() and str() calls the __str__ method
class Employee: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age
    def __str__(self):
        return f"Employee name is {self.name} and employee's age is {self.age}"

employeeObject = Employee('Max', 26)

print(employeeObject)
print(str(employeeObject))

#__new__ method - static method which is called before init when creating new object
#responsible for creating and returning the new instance of class
class Emplyee:
    def __new__(cls, *args, **kwargs):
        print("Creating a new instance of Employee")
        return super().__new__(cls)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Employee name is {self.name} and employee's age is {self.age}"

# Creating an instance of the Person class
person1 = Employee("Jay", 25)
print(person1)
