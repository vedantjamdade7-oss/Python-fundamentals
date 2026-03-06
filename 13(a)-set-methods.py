# set methods
# 1. union - combine element from 2 set

set1 = {1,2,3}
set2 = {3,4,5}
union = set1.union(set2)
print(union)

set1 = {1,2,3}
set2 = {3,4,5}
union = set1 | set2
print(union)

# 2. Intersection - common elements

set1 = {1,2,3,4}
set2 = {3,4,5,}
intersection = set1.intersection(set2)
print(intersection)

intersection = set1 & set2
print(intersection)

# 3. Different - element present in first set only but ont in second set

set1 = {1,2,3,4}
set2 = {3,4,5,}
difference = set1.difference(set2)
print(difference)

difference = set1 - set2
print(difference)

# 4.symmertic Difference - element in either set but not in both

set1 = {1,2,3,7}
set2 = {3,4,5,6}
sdiff_set = set1.symmetric_difference(set2)
print(sdiff_set)

sdiff_set = set1 ^ set2
print(sdiff_set)