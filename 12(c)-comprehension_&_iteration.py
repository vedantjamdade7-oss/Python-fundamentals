# Dictionary comprehension - It is a concise way to create dictionaries.

# syntax:
# {key_exp:value_exp for item in iterable if condition}

# create a square in Dictionary

# square 
dict = { x:x*x for x in range (1,9)} # x:x*x is key:value pair , for x is looping througnth range(1,9)
print(dict)

# cube
dict_cube = { x:x*x*x for x in range (1,9)}
print(dict_cube)

# multiplying by 2 
dict = { x:x*2 for x in range (1,9)}
print(dict)

# -----------------------------------------------------------------------------------------------------------------------------

# Dictionary iteration - Looping Through Dictionary

student = {
    1:"class-x",
    'name':'karan',
    'age': 20,
    'city':'mathura'
 }
print("---------")

# loop through keys
for key in student:
    print(key)
print("---------")

# loop thriugh values
for value in student:
    print(student[value])

print("---------")

# loop through value : using value () method
for value in student.values():
    print(value)

print("---------")

# loop through key : using key () method
for key in student.keys():
    print(key)

print("---------")

# loop through both key and values
for key,value in student.items():
    print(key,value)
