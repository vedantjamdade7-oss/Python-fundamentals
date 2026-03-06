# 4. Nested if-else statement
# if-else inside if-else statement
# multiple condition depend on each other

# Q : Check the positive , negative and zero. where positive is even/odd

number = int(input("Enter a number :"))
    
if number > 0: #checking positive number
    if number % 2 == 0:
        print("This is a positive and even number")
    else:
        print("This is a positive and odd number")
else:
    if number == 0:
        print("The number is zero .")    
    else:
        print("The number is negative .")
