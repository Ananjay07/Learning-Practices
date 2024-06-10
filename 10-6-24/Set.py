#SET - It is a set is an unordered collection of unique elements
#It cannot have duplicate values and order of elements is undefined
#It is used for used for tasks that involve membership testing, removing duplicates from a sequence, and performing mathematical operations like union, intersection, and difference
set1 = {1,2,3,4,5}
#or
set2 = set([6,7,8,9,0])
print(set1)
print(set2)

#Operations
#1) Union(|): Join two or more sets
union = set1 | set2
print("Union:", union)

#2) Intersection (&): Find common elements in both sets
num = {1,2,3,4}
odd = {1,3,5,7}
print("Intersection:", num & odd)

#3) Difference (-): elements present in the first set but not in the second set
print("Difference:",num - odd)

#4) Symmetric Difference (^): elements that are present in either set but not in both sets
print("Symmetric Difference:", num ^ odd)


#Methods: 
#add(element) - Add element to set
print(set1)
set1.add(9)
print(set1)

#remove(element) - Remove element from set. Error occurs if element not found
print(set1)
set1.remove(9)   
print(set1)

#discard(element) - Remove element from set. Error does not occur if element not found
print(set2)
set2.discard(1)
set2.discard(7)
print(set2)

#pop() - remove and return arbitrary element from set
print(set1)
set1.pop()
print(set1)

#clear() - remove all elements from set
set2.clear()
print(set2)

#copy()
copyset = set1.copy()
print(copyset)

#update()

#issubset(other_set) - check if all elements of set are present in specified set
num1 = {1,2,3}
num2 = {1,2,3,4,5,6,7}
print("set1:", num1)
print("set2:", num2)
print("issubset:", num1.issubset(num2))

#issuperset(other_set) - check if set 1 contains all elements of another set
print("issuperset:", num1.issuperset(num2))

#isdisjoint(other_set) - check if set has no elements in common with another set
print("isdisjoint:", num1.isdisjoint(num2))