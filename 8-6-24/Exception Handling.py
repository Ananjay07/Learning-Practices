#Exception handling is used for dealing with unexpected errors or issues that may arise during program execution
#It allows you to gracefully handle these errors and provide messages to the user. 

#try and except block
try:
  result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
  print("You cannot divide by zero")
else:
  print(f"The result is: {result}")

#try and finally block
#finally block will always execute programs regardless of whether an exception occurs in the try block or not.
try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: File not found.")
except IOError:
    print("Error: An I/O error occurred.")
else:
    print("File read successfully.")
finally:
    file = open("example.txt", "r")
    file.close()
    print("File closed.")

#Built-in Exceptions:
#Syntax error
#Indentation error
#Name error
#Type error
#Value error
#ZeroDivision Error

#Using except with specific exception
try:
    x = int(input("Enter a number: "))
    y = 10 / x
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Can't divide by zero!")
else:
    print(f"Result: {y}")

#Exceptions at different levels
#Local level:
def divide(a, b):
  try:
    result = a / b
  except ZeroDivisionError:
    print("Cannot divide by zero!")
    return None 
  else:
    return result

result = divide(10, 2)
print(result)
result = divide(10, 0)
print(result)

#Intermediate Level:
def process_data(data):
    try:
        result = 10 / data
    except ZeroDivisionError:
        raise ValueError("Invalid data") from None

try:
    process_data(0)
except ValueError as e:
    print("Error:", e)

#Global Level:
def main():
    try:
        result = 10 / 0
    except ZeroDivisionError :
        print("An error occurred: Cannot divide by zero")

if __name__ == "__main__":
    main()