#  Module and Package in Python

# Modules also Known as Libraries in python.

#  What is a Module in Python?

# A module is a single Python file (.py) that contains functions, classes, or variables.
# It allows you to organize your code into separate files for better maintainability and reusability.

# Example:-
# Let's say we have a module named 'calculator.py' with the following content:
# calculator.py (This is a module)
# calulator.py (This is a module)

# def add(a, b): This part is new in the recent edit
#     return a+b

# def subtract(a, b): 
#     return a - b

# def multiply(a, b):
#     return a * b

# Importing a Module
# you can import a module into your python script using the "import" statement.

# import math

import math
import calculator

print(calculator.add(5, 3))
print(calculator.subtract(10, 4))


a = 36
print(math.sqrt(a))

# import specific function from library

from math import factorial
b = 4
print(factorial(b))

# installed new modules/library
# pip install <library_name>

# import pandas as pd

# Packages in python
# A package is a collection of related modules organized in a directory hierarchy.

# Example:
# Let's say we have a package named 'data_analysis' with the following structure:
# data_analysis/
#  __init__.py
#  statistics.py
#  visualization.py
# you can import modules from a package using the dot notation.

# from data_analysis import statistics
# from data_analysis.visualization import plot_graph
# In this example, 'data_analysis' is the package and 'statistics and 'visualization' are modules within that package.

# Importing from another module
from mymodule import person1, person2

print(person1['age'])
print(person1['name'])
print(person2['name'])
print(person2['age'])
print(person1)
print(person2)


