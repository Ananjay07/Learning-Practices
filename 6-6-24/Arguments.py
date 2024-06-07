#Positional arguments - function is defined in an order
def area_of_rect(l,b):
    return l * b
print(area_of_rect(4,5))

#Keyword Argument - keyword can be given when calling the function
def greet(name, message=" "):
    print(message,name)
print(greet(name="Jay",message="Helloo"))

#default argument - predefined values are set (shown if no values are input while calling the function)
def greet(name="Raj"):
    print("Hey",name)
print(greet())

#variable length argument (*arg) - can take unlimited number of data as input and perform the function
def sum(*num):
    a = 0
    for i in num:
        a = a + i
    return a
print(sum(1,2,3,4,5,6,7,8,9))

#keyword variable length argument (**kwarg)- 
