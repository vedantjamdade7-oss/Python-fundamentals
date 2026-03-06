# Function in python
# This is used to group a set of statements so that they can be run more than once.

# 1. create a function to print greeting message
def greetings():
    print("I have to stand alone to win!")

# call function (use function)
greetings()


# 2. create a function to add 2 number

def add2numbers(a,b): # parameter (a,b)
    result = a + b
    print("The sum is :", result)

# call above sum function
add2numbers(8,9)     # arguments (8,9)

add2numbers(a=60 , b=40)     

add2numbers(b=10 , a=110)  