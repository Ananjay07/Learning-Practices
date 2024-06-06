#passing a func as argurment
#one function is used as an argument(variable) in another function
def add(a, b):
   return a + b
def mult(a, b):
   return a * b
def math(func, a, b):
   return func(a, b)

print(math(add,5,9))    #add func used in math
print(math(mult,5,8))   #mult func used in math