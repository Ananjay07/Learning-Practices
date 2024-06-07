#instance variable - attributes that are specific to each object of a class
#separately maintained for each and every object instance of the class
#"self" is used
class MyClass:
    def __init__(self): 
        
      self.msg = "This is stored in an instance variable."  #self.msg is instance variable
  
    def func(self): 
        print('This was printed by an instance method.') 
        return self.msg 
  
obj = MyClass()
print(obj.func()) 

##class variable -  shared among all objects of a class
#"cls" is used
class MyClass1:
    cls_msg = "This is stored in an class variable."
    def __init__(self): 
        self.msg = "This is stored in an instance variable." 
  
obj = MyClass1()
print(MyClass1.cls_msg) 
print(obj.cls_msg)