#lambda function - way of defining short anonymous functions
# lambda arguments : expression
area = lambda x,y : x*y
print(area(6,8))

function = lambda func : print(f"{func} is a function")
print(function("lambda"))