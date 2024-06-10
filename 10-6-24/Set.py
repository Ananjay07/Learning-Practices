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

