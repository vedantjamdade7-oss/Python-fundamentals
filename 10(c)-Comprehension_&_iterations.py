#  List Comprehension
# List comprehension provides a concise way to create lists.

# create a list of squares

squares = [x**2 for x in range(1,6)] # square of number from 1 to 5
print(squares) 

# filter even numbers

even = [x for x in range(1,10) if x % 2 ==0] # even numbers from 1 to 9
print(even)

# apply function to each element of a list
mylist = ["apple","mango","cherry"] 

uppercase = [lst.upper() for lst in mylist] # convert to uppercase
print(uppercase)

# flatten a nested list 

nestedlist = [[1,2],[3,4],[5,6]] # nested list

def flatten_list(lst): # function to flatten list
    return [item for sublist in lst for item in sublist] # flatten logic ('item from sublist in lst' is added to new list [[1,2],[3,4]] -> [1,2,3,4]),('for item in sublist' is nested loop to access each element of sublist for Ex- [[1,2],[3,4]], first sublist is [1,2] then second sublist is [3,4])
final_list = flatten_list(nestedlist)
print(final_list)

# meaning
# first [1,2] -> 1,2
# first [3,4] -> 3,4
# first [5,6] -> 5,6

# ------------------------------------------------------------------------------------------------------------------

# List iterations - It is the process of Lopping throught each item in the list.

fruits = ["apple","mango","cherry"]

# using for loop

for fruits in fruits:
    print(fruits)

# while loop

fruits2 = ["apple","mango","cherry"]
print('length of list',len(fruits2))
index = 0
while index < len(fruits2):
    print(fruits2[index])
    index += 1