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
# When a function reaches a return statement, it stops executing and sends the result back.
# If a function doesn't have a return statement, it returns None by default.
def display2():
    return "hello world"

a = display2()
print(a)
# Returning Different Data Types
# Functions can return any data type, including lists, tuples, dictionaries, and more.
def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

print(display2())
# Function definitions cannot be empty. If you need to create a function placeholder without any code, use the pass statement:
def average(nums):
    pass

# Default Parameter Values:
#   You can assign default values to parameters. If the function is called without an argument, it uses the default value:
def my_func(name = "amin", age = 22):
    print("hello",name, age)

my_func()
my_func("ali")
my_func(20)  # ???!!!!!!
my_func("reza", 30)
# You can send arguments with the key = value syntax.
# This way, with keyword arguments, the order of the arguments does not matter.
my_func(name="arash", age= 40)
my_func(age= 50, name="mamad")
# Positional-Only Arguments
"""You can specify that a function can have ONLY positional arguments.
To specify positional-only arguments, add , / after the arguments:"""
def my_func2(name, age,/):
   print(name, age)

my_func2("amin", 22)
# my_func2(name = "x", age= y)   can not ????

# To specify that a function can have only keyword arguments, add *, before the arguments:
def my_func3(*, name):
   print("hello", name)
my_func3(name= "xx")
# my_func3("xxxx")  can not ??????

# You can combine both argument types in the same function.
#   Arguments before / are positional-only, and arguments after * are keyword-only:
def my_func4(name, age,/,*,lasname):
   print(f"hello {name} {lasname} you have {age}")

my_func4("amir", 30, lasname="amiri")

# Passing Different Data Types
"""You can send any data type as an argument to a function (string, number, list, dictionary, etc.).
The data type will be preserved inside the function:"""
def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)
def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)


