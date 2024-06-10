#List Comprehension - It consists of brackets containing the expression, which is executed for each element along with the for loop to iterate over each element in the list
#It gives shorter syntax when you want to create a new list based on the values of an existing list
#eg1)
numbers=[5,7,9]
sqrd = [x**2 for x in numbers]  #all elements in the numbers list is squared
print(numbers)
print(sqrd)

#eg2)
even_numbers = [x for x in range(20) if x % 2 == 0]
print("Even numbers:", even_numbers)      #all even numbers from range of 0-20 are printed

#eg3)
words = ["hello", "world", "python", "code"]
print("Words:", words)
uppercased_words = [word.upper() for word in words]     #all string in elements in words list is converted to uppercase format
print("Uppercased words:", uppercased_words)