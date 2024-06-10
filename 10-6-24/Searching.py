#Searching - iterating through the list sequentially to find a specific element
person = ["Lewis", "Max", "Perez", "Charles", "Alonso"]
print("List:", person)
has_Lewis = "Lewis" in person
print("Lewis in list: ", has_Lewis)

element_to_find = "Charles"
found = None
for i in person:
    if i == element_to_find:
        found = i
        break
print("Found element:",found)