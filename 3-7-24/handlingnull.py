#NULL VALUES 
# They are undefined data points in a dataset

#identifying null values:
# isnull() - returns a DataFrame of the same shape as the input, True if it's a null value and False otherwise
df.isnull()
# info() - provides a concise summary of the DataFrame
df.info()

#handling null values:
