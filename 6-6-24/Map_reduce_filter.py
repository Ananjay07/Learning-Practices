#map func - func applies to all elements of a list/tuple
num = (1,2,3,4,5,6)
sum = map(lambda x : x+x,num)
print(list(sum))

#filter func - filter elements that satisfies a condition
div = filter(lambda x : x % 2 == 0, num)
print(list(div))

#reduce func - performs function iterating through each element as a loop
from functools import reduce 
sum = reduce(lambda x, y: x + y, num)
print(sum)
