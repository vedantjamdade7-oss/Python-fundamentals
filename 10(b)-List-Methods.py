# List Methods

# 1 append
fruits = ["apple", "banana", "orange"]
fruits.append("cherry")

print(fruits)

# 2 extend
fruits1 = ["kiwi", "mango"]
fruits.extend(fruits1)
print(fruits)

# 3 insert
fruits2 = ["apple", "banana"]
fruits2.insert(0,"mango")
print(fruits2)

# 4 remove
fruits3 = ["apple", "banana", "mango"]
fruits3.remove("mango")
print(fruits3)

# 5 clear
fruits4 = ["apple", "banana"]
fruits4.clear() # empty list
print(fruits4)

# 6 finding index
fruits5 = ["apple","orange","banana","mango","banana"]
index = fruits5.index("orange")
print(index)

# finding index - within a range
index = fruits5.index("banana",2)
print(index)

# 7 count element
fruits6 = ["apple","mango","cherry","mango"]
count = fruits6.count("mango")
print(count)

# 8 Reverse list
fruits7 = ["apple","mango","cherry",]
fruits7.reverse()
print(fruits7)

# Importances------------------

# 9 sorting list
numbers = [40,10,50,30,60,20]
numbers.sort() # asc order
print(numbers)

# sort in desc order
numbers.sort(reverse=True)
print(numbers)

# sorting string in a list
fruits8 = ["apple","mango","cherry","kiwi"]
fruits8.sort()
print(fruits8)

fruits8.sort(key=len)
print(fruits8)

# 10 pop with index
num = [10,20,30,40]
popped = num.pop(2) # used in real life
print(popped)
print(num) 

last = num.pop()
print(last)
print(num)

# 11 copying list
fruitss = ["apple","mango","cherry"]
myfruits = fruitss.copy()
print(myfruits)

# copying list - modifying the copy does not affect the original
myfruits.append("blueberry")
print(myfruits)

# 12 Join List

# using + oprator
list1 = [1,2]
list2 = ["a","b"]

# list3 = list1 + list2
# print(list3)

# print("using append method")

# for x in list2:
#     list1.append(x)
# print(list1)

print("using extend method")
list1.extend(list2)
print(list1)