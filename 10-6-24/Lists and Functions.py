#List
#Types of list:
#1) Ordered list
#2) Indexable
#3) Mutable
#4) Heterogeneuos
#5) Dynamic
#6) Iterable
#7) Methods and Functions 

#Methods and functions of List:
#Append - Add an element to the end of the list
person = ["Lewis","Max","Charles"]
print("List:", person)
person.append("Alonso")
print("Append: ", person)

#Insert - Insert element at a specific position of the list
person.insert(2, "Perez")    #Element is inserted at index 2
print("Insert: ", person)

#Remove - Remove a specific element
person.remove("Alonso")
print("Remove: ", person)

#Copy - create copies of lists
person_copy = person.copy()
person_copy[1] = "Yuki"
print("Original: ", person)
print("Copy: ", person_copy)

#Count - It give the number of occurance of an element
print("1st count: ", person.count("Lewis"))
person.append("Lewis")
print("2nd count: ", person.count("Lewis"))

#Extend - add elements from another iterable to current list
person_2 = ["Sainz","Daniel"]
person.extend(person_2)
print("Extended list: ", person)

#Index - Get index of the an element in a list
print("Index of Charles: ", person.index("Charles"))

#Sort - Sort in an order
person.sort()     #It comes in ascending order by default
print("Sort: ", person)

#Reverse - Reverse the order of elements
person.reverse()
print("Reverse: ", person)

#clear - remove all elements
person.clear()
print("Clear: ", person)

#Pop - remove element at a position
person_2.pop()   #last element is popped by default
print(person_2)