"""
A function is a block of code which only runs when it is called.
A function can return data as a result.
A function helps avoiding code repetition.
"""
# create:
def display():
    print("hello world")

display()
def fahrenheit_to_celsius(f):
    print((f-32)*5/9)
fahrenheit_to_celsius(100)
fahrenheit_to_celsius(50)
# Functions can send data back to the code that called them using the return statement.
# When a function reaches a return statement, it stops executing and sends the result back:
def display2():
    return "hello world"

a = display2()
print(a)
print(display2())
# Function definitions cannot be empty. If you need to create a function placeholder without any code, use the pass statement:
def average(nums):
    pass





