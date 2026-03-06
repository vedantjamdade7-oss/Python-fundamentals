# Recursive Function
# A recursive function is a function that calls itself in order to solve a problem.

# Example: Calculate factorial of a number using recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5)) # output: 120