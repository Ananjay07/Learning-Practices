#Abstraction - The principle of exposing only the essential features of an object and hides unnecessary implementation details
class Students:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks     #here marks is a private attribute which is the only required value
    
    def get_marks(self):
        return self.marks
    def set_marks(self, new_marks):
        if new_marks > 0:
            self.marks = new_marks
        else:
            print("Invalid salary")

p1=Students("Max",20,40)
print(p1.get_marks())
p1.set_marks(80)
print(p1.get_marks())