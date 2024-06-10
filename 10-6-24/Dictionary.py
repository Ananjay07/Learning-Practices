#Dictionary: A dictionary in Python is an unordered collection of key-value pairs 
#It is mutable - add, modify, remove is possible after creation
#It is used for storing and retrieving data
dictionary = dict()
person = {"name": "Lewis", "age": 39,}
print(person["name"])
#or
print(person.get("age"))

#Methods:
#keys(): returns a view object having dictionary's keys
print("Keys:", person.keys())

#values(): Return the dictionary's values
print("Values:", person.values())

#items(): displays a list of all values in the dictionary
print("Items:", person.items())

#get(key,default): gives value for a specific key. If it does not exist, default value provided is shown
print("Get:", person.get("name"))

#pop(key,default): removes a key-value pair from dict
print("Pop:", person.pop("age"))
print("After pop:", person.items())

#clear(): removes all key-value pairs
my_dict = {'apple': 1, 'banana': 2, 'orange': 3}
print(my_dict)
print(my_dict.clear())

#copy(): copy a dictionary
new_person = person.copy()
print("Copied:", new_person)

#Dictionary COmprehension - Concise way to create a new dictionary from an iterable
nums = [2,4,6,8]
sqr = {num:num**2 for num in nums}
print(sqr)

#separate keys and values are put together using disctionary comprehension
keys = ['a', 'b', 'c', 'd', 'e'] 
values = [1, 2, 3, 4, 5]

new_dict = {key: value for key, value in zip(keys, values)}
print(new_dict)

#Nesting dictionaries - Dictionaries can contain other dictionaries as values, creating nested structures
person = {
    'name': 'Lewis',
    'age': 90,
    'contact': {
        'email': 'lewis@hmail.com',
        'phone': '1234567890'
    }
}

print(person['contact']['email']) 