# Tuple Operation

# concatenate - join tuple

tuple1 = (1,2,3,4,5)
tuple2 = ('a','b')

tuple3 = tuple1 + tuple2
print(tuple3)

# Repetition - repeat the tuple elements

tuples = ("hello",)*3
print(tuples)

tuple4 = ('a','b')*2
print(tuple4)

# Membership - to check if an element is present in the tuple or not

numbers = (10,20,30,40,50)
print(30 in numbers)
print(60 in numbers)

# Tuple packing and unpacking 

# Packing - The process of assing multiple values into a single tuple variable.
a = "vedant"
b = 20
c = "Engineer"

tuple_pack = a,b,c
# print(tuple_pack)

# Unpacking - The process of extracting value from a tuple into multiple variables.
name,age,profession = tuple_pack
print(name)
print(age)
print(profession)

# Tuple iteration - It is the process of looping through each item in the tuple.


# for loop
fruits = ('apple','mango','cherry')

for i in fruits:
    print(i)

# while loop

i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

# -------------------------------------------------------------

# Tuple function

numbers = (2,3,4,5,6)
# len
print(len(numbers))

# sum
print(sum(numbers))

# min,max
print(min(numbers))

# sort
print(sorted(numbers)) # tuple is now list


# Note: 1. you can't change tuple value but you can convert it to list and then back to tuple after making changes.
#       2. tuple are immutable so we cannot use sort() method directly on tuple.
#       3. sorted() function returns a list instead of tuple.
#       4. To convert it back to tuple we can use tuple() constructor.
#       5. tuple() constructor can also be used to create a tuple from an iterable like list, string,etc.
   
#  Difference Between Tuple Operation and Tuple Function.

# | Feature | Tuple Operation | Tuple Function           |
# | ------- | --------------- | ------------------------ |
# | Uses    | Operators       | Function names           |
# | Symbols | `+`, `*`, `in`  | `len()`, `sum()`         |
# | Purpose | Perform actions | Get information / result |
# | Example | `t1 + t2`       | `len(t)`                 |


