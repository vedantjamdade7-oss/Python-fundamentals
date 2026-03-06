# Lambda Funtion
# Lambda function is a small anonymous function that can take any number of arguments, but can only have one expression.

# Syntax:
# lambda arguments : expression

# Example 1: A lambda function that adds 10 to the number passed in as an argument
x = lambda a : a + 10
print(x(5)) # o/p: 15

# Example 2: A lambda function that multiplies two numbers
y = lambda a, b : a * b
print(y(5, 6)) # o/p: 30

# Example 3: A lambda function that returns the maximum of two numbers
z = lambda a, b : max(a, b)
print(z(10, 20)) # o/p: 20