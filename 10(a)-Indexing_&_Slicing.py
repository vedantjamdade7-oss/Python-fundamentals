#  List - Indexing

list = [12,23,34,56,67,78]
#index: 0  1  2  3  4  5
print(list[0]) # 1-element
print(list[1]) # 2-element
print(list[2]) # 3-element
print(list[3]) # 4-element
print(list[4]) # 5-element
print(list[5]) # 6-element
print(list[-1]) # last-element

# ---------------------------------------------------------------------------

# List - slicing

list = [12,23,34,56,67,78]
#index: 0  1  2  3  4  5
#index:-6 -5 -4 -3 -2 -1

# syntax
# list_name = [star:stop:step]

# first 3 element
print(list[0:3])

# start to index 2
print(list[::3])

# all alternate element
print(list[0::2])

# negative indices
print(list[-4:-1])

# Revers list
print(list[::-1])
print(list[::-5])
