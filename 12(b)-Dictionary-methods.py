# Dictionary methods

student = {
    1:"class-x",
    'name':'vedant',
    'age': 20,
    'city':'nagpur'
 }

# 1. keys - returns all keys
print(student.keys())

# 2. values - returns all values 
print(student.values())

# 3. items - returns all key:value paris 
print(student.items())

# 4. get - used to access value of particular key
print(student.get("name"))
print(student.get("age"))
print(student.get("email")) # not giving error

# 5.update() - To add new key:value pair or to update existing key value
student.update({'email':"karan@gmail.com"})
print(student)

# 6. pop() - removes the key:value pair and return the value of the key
var = student.pop('email')
print(var)
print(student)

# 7. popitem() - removes the last inserted key:value pair and return as tuple 
var2 = student.popitem()
print(var2)

# 8. clear() - remove all items from the dictionary
student.clear()
print(student)


# Note: Dictionary is mutable so we can change its value and add new key:value pair.