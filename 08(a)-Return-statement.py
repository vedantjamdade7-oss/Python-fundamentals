# Return statement
# Funtion with Return Statement is used to send back a result from a function to the caller.

def add2num(a,b):
    return a + b

sum2num = add2num(10,23)
print(sum2num)

# Function to convert celsius to fahrenheit
def celsius_to_fahrenheit(celsius):
    fahreheit = (celsius * 9/5) + 32
    return fahreheit


# call function
temp_f = celsius_to_fahrenheit(10)
print(temp_f) # o/p: 50.0