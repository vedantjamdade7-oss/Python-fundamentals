# Formatted string

# 1.old style formatted - % operator

name = "vedant"
age = 20
print("my name is %s and i'am %d" % (name,age))
# %s , %d are placeholder for the string and integer values.

# --------------------------------------------------------------------------------

# str.format()method

# 2. new style formatted - str.format() method.
name = "vedant"
age = 20

print("my name is {} and i am {}" .format(name,age))

# you can reference variable by index or keyword
print("my name is {0} and i am {1}" .format(name,age))
print("my name is {name} and i am {age}" .format(name="karan",age=20))

# --------------------------------------------------------------------------------

# F - strings (formatted string literals)

# 3. f- strings (formatted string literals) - current version of python uses mostly.

name = "vedant is a billinaire"
age = 21

print(f"who is vedant? {name} and how old he is? , he is just {age}")

print(f"who is vedant? {name} and how old he is? , he is just {age} in 4 years he will be {age+4}")