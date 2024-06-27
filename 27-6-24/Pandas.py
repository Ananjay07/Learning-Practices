#Pandas - Library for Handling Structured Data in Python
#Features: 
#1) DataFrames and Series
#2) Comprehensive Data Operations
#3) Handling Missing Data
#4) Integration with Other Libraries

#install pandas
# pip install pandas

import pandas as pd
#creating pandas series from lists, arrays, and dictionary
list = [20, 30, 40, 50]
p = pd.Series(list, index=[1, 2, 3, 4])
print("Series from list:")
print(p)

import numpy as np
array = np.array([1.1, 2.2, 3.3, 4.4])
p_array = pd.Series(array, index=["x", "y", "z", "w"])
print("Series from array:")
print(p_array)

dict= {"Maths": 80, "English": 81, "Physics": 90}
p_dict = pd.Series(dict)
print("Series from dictionary:")
print(p_dict)

#Attributes
print("Index:", p.index)
print("Values:", p.values)
print("Data type:", p.dtype)
print("Size:", p.size)

#Methods
print("First two elements:")
print(p.head(2))
print("Last two elements:") 
print(p.tail(2))
print("Sorted values:") 
print(p.sort_values())
print("Mean of the Series:")
print(p.mean())