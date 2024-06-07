#normal method - access instance data through self parameter
class Myclass:
    def normal_method(self):   #self is first parameter
        print("Hello world")
    
obj = Myclass()
obj.normal_method()

#class method - bound to the class parameter using cls parameter
#they can access and modify class attributes
class Myclass:
    class_var=0
    def increment(self):
        Myclass.class_var +=1

print(Myclass.class_var)
obj=Myclass().increment()
print(Myclass.class_var)

#Static Method - defined within class but not associated with any specific object
#"self" or "cls" is not used
class Maths:
    @staticmethod
    def even(num):
        return num%2==0
    
    @staticmethod
    def odd(num):
        return num%2==1

print(Maths.even(2))
print(Maths.even(9))
print(Maths.odd(5))
print(Maths.odd(8))