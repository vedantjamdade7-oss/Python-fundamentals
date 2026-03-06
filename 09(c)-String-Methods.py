# String Methods
# String Methods are built-in function that perform specific operations on string data types.

# 1. lower() - coverts all char in to lowercase
text = "Hello World"
print(text.lower())

# 2. upper() - coverts all char in to uppercase
print(text.upper())

# 3. strip() - remoces the spaces from the beginning and end of the string
name = "  Vedant  "
print(name.strip())

# 4. replace() - replace a specified character with another character
text = "I love Java"
print(text.replace("Java", "Python"))

# 5. split() - splits the string into a list of substrings based on a separator
sentence = "Python is easy"
print(sentence.split())

# 6. join() - joins a list of strings into a single string with separator.
words = ["Python", "is", "fun"]
print(" ".join(words))

# 7. find() - returns the index of the first occurrence of a substring.
text = "Hello Python"
print(text.find("Python"))

# 8.count() - counts the number of substring occurrences in a strings.
text = "banana"
print(text.count("a"))

# 9. len() - returns the length of the string.
text = "Python"
print(len(text))

# 10. isalpha() - it is used to check the starting characters of the string are alphabetic or not.
print("Python".isalpha())

# 11. isdigit() - it is used to check whether all the characters in the string are digits or not.
print("123".isdigit())
