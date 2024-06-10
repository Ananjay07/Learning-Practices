#Indexing
#1) Positive Indexing - Access elements from beginning
person = ["Lewis", "Max", "Perez", "Charles", "Alonso"]
print("1st:", person[0])
print("2nd:", person[1])
#2) Negative Indexing - Access elements from end
print("Last:", person[-1])
print("2nd last:", person[-2])
#3) Retrieve - Access element at specific index
print("Middle:", person[2])
#4) Update - Change value of element at specific index
person[2] = "Sainz"
print("Update:",person[2])

#Slicing
#1) Positive slicing - select element from specific index to another specific end index
print("2nd to 4th:", person[1:4])

#2) Negative slicing - select element from a specific index to another from the end
print("Last 3:",person[-3:])

#3) Retrieve
print("First 3:", person[0:3])

#4) Update
person[2:4] = ["Yuki", "George"]
print("Update:", person)

#5)Delete and Insert
del person[2:4]
print("Del:", person)