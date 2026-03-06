# Indexing in Strings
# Indexing is used to access individual characters in a string.
myname = "VEDANT"
print(myname[0])  # first character of str
print(myname[1])  # 
print(myname[2])  #
print(myname[3])  #
print(myname[4])  #
print(myname[5])  # sixth character of str


name = "my self vedant"
print(name[-1])
print(name[13])

# ------------------------------------------------------------------------------------------

# Slicing in Strings
# slicing is used to access a substring from a string.
name = "VEDANT"
#indax: 012345
#       654321
print(name[0:3])
print(name[0:3:1])
print(name[0:4:1])
print(name[0:5:2])
print(name[0:5:3])
print(name[0:4:2])
print(name[3:5:1])
print(name[3:5:2])
print(name[-1])
print(name[-1:-6:-1])
print(name[0::2])
print(name[0::3])
print(name[::])
print(name[-1:-6])
print(name[::-1])