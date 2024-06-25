#NUMPY
#NumPy (Numerical Python) is a library for numerical operations in Python

#install numpy using:  pip install numpy

import numpy as np
#NumPy Arrays:
# Creating arrays:
arr = np.array([1, 2, 3, 4, 5])
print(arr) 

#a list can be converted to array using np.asarray()

# Create a 1D array of ones
ones = np.ones(5)
print(ones) 

# Create a 1D array of zeros
z = np.zeros(5)
print(z) 

# Create a sequence till the given number
ar = np.arange(5)
print(ar) 
# Create an array with evenly spaced values between two numbers
ls = np.linspace(0, 10, 5)
print(ls) 

# Create a 3x3 identity matrix
a = np.eye(3)
print(a)

#1) Shape
#1D array 
a = np.array([1,2,3,4])
print(a.shape)
#2D array
b = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(b.shape)

#2) Size - number of items in array
c = np.array([1, 2, 3, 4, 5, 6])
print(c.size) 

#3) dtype - shows the datatype of the array
# Integer array
d = np.array([4, 7, 10, 12, 1, 2])
print(d.dtype) 
# Float array
e = np.array([1.0, 2.0, 3.0])
print(e.dtype)

#OPERATIONS
ar1 = np.array([1,3,5,7,9])
ar2 = np.array([2,4,6,8,10])

sum = ar1 + ar2         #addition
print(sum)

diff = ar2 - ar1        #subtraction
print(diff)

pr = ar1 * ar2          #multiplication
print(pr)
pr1 = ar1 * 2
print(pr1)

div = ar2 / ar1         #division
print(div)
div1 = ar2 / 2
print(div1)

ar3 = np.array([4,9,16])
print(np.sqrt(ar3))     #squareroot

print(np.exp(ar3))      #exponential

#INDEXING - a way to access individual elements or subsets of the array data
a1 = np.array([1,2,3,8,9,10])
#Basic indexing
print(a1[4])

#Fancy Indexing
indices = np.array([0, 2, 4])
print(a1[indices])

#Boolean indexing
print(a1[a1 > 3])

#SLICING - extract a subset or a view of an array
a1 = np.array([1,2,3,8,9,10])
print(a1[2:5])  
print(a1[:3])   
print(a1[5:])   

print(a1[::2])
print(a1[::-1]) 

#a1[1:4] = 10
print(a1)

#ARRAY MANIPULATION
print(a1.shape)  
#Reshape - changing dimensions 
# Reshape to a 2D array
twod=a1.reshape(2, 3)
print(twod)

# Reshape to a 3D array
threed = a1.reshape(2, 1, 3)
print(threed)

#Flatten - change multidimensional to 1D
print(a1.ravel())

#STACKING ARRAY - process of combining arrays along a new axis
s1 = np.array([1, 2])
s2 = np.array([3, 4])

print(np.hstack((s1, s2)))              # Stack arrays horizontally

print(np.vstack((s1, s2)))              # Stack arrays vertically

print(np.stack((s1, s2), axis=1))       # Stack arrays along a new axis

#Create a 2D array
a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]])

# Split the array horizontally into 2 sub-arrays
left, right = np.hsplit(a, 2)
print("Horizontal split:")
print("Left sub-array:\n", left)
print("Right sub-array:\n", right)

#APPENDING
a = np.array([1, 2, 3])
b = np.append(a, [4, 5])
print(b)  

c = np.array([[1, 2], [3, 4]])
d = np.append(c, [[5, 6]], axis=0)
print(d)

#INSERTING
a = np.array([1, 2, 3, 4, 5])
b = np.insert(a, 2, [10, 20])
print(b) 

c = np.array([[1, 2], [3, 4]])
d = np.insert(c, 1, [10, 20], axis=1)
print(d)

#DELETING
a = np.array([1, 2, 3, 4, 5])
b = np.delete(a, [0, 2])
print(b) 

c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.delete(c, 1, axis=1)
print(d)

#RESIZING
a = np.array([1, 2, 3, 4, 5])
b = np.resize(a, (3, 3))
print(b)