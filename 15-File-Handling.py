# FILE HANDLING IN PYTHON
# File handling is an important aspect of programming that allow us to read from and write to filed on our system.
# In python we have several built-in functions and methods to handle files easily.

# mode: r - read, w - write, a - append, rb-read binary/wd - write binary

# 1. Opening a file 
# The first step in file handling is to open a file using the open() function. This function takes two arguments: the file path and the mode in which the file is to be opened.
file = open('example.txt', 'w') # 'w' mode is for writing

# 2. writing to a file 
file.write('Hello, this is an example of file handling in python.\n')

file.write('we can write multiple line to a file using the write() methods.\n')

# 3.Closeing a file 
file.close()
# It is important to close a file after we are done with it to free up system resources.

# 4. Reading from a file 
file = open('example.txt', 'r') # 'r' mode is for reading 
content = file.read()
print(content)

file.close()

# 5. using with statement
# The with statement is used to handle file in python. It automatically take care of closing the file after the block of code is executed.
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# 6. Other file modes
# 'a' - append mode, used to add content to end of the file without overwriting existing content.
with open('example.txt', 'a') as file:
    file.write('This line is added in append mode.\n')

# 'x' - exclusive creation mode, used to create a new file. If the file already exists, it will raise an error.
with open('newfile.txt', 'x') as file:
    file.write('This is a new file created using exclusive creation mode.\n')

# 7. Reading line by line
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip()) # strip() method is used to remove leading and trailing whitespace characters including new line character.

# 8. File Handling Errors
# When handling files, it is important to handle potential errors that may occur, such as file not found errors or permission errors. This can be done using try-except blockes.
try:       # attempting to open a file 
    with open('nonexistentfile.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:  # handling file not found error
    print("Error: The file does not exist.")
except PermissionError:    # handking permission error
    print("Error: you do not have permission to access this file.")

