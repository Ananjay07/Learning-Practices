#Tuples - They are used to store multiple items in a single variable
#It is a collection which is ordered and unchangeable(immutable)
#They allow duplicate values and can store different datatypes
#written in ()
cars = ("BMW", "Mercedes", "Porsche", "Volvo")
print(cars)

#To add elements, first convert the tuple into list, add element and convert back to tuple
carlist = list(cars)
print("List:",carlist)
carlist.append("Maserati")
cars = tuple(carlist)
print(cars)

#deleting a tuple:
#del cars
#print(cars)

#joining tuples
cars2=("Lamborohini","McLaren")
print(cars+cars2)

#multiply tuple
car = cars * 2
print(car)

#Built-in Functions
#len - length of tuple
print("Length:", len(cars))

#sum - sum of elements
num = [4,3,2,1,5]
print("Sum of no:", sum(num))

#max - largest element
print("Largest no:", max(num))

#min - smallest element
print("Smallest no:", min(num))

#sorted - sort elements
print("Tuple:", num)
print("Sorted tuple:", sorted(num))