#Encapsulation - principle of bundling data and methods within a single class
#It hides internal implementation details of object and provides well defined interface
#Encapsulation is done using getter and setter methods.
class Employee:
    def __init__(self):
        self.salary = 0
        
    def set_salary(self, salary):
        self.salary = salary
        
    def get_salary(self):
        return self.salary

e = Employee()
e.set_salary(80000)
print(e.get_salary())