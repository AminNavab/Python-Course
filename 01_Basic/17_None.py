# None is a special constant in Python that represents the absence of a value.
# Its data type is NoneType, and None is the only instance of a NoneType object.
x = None
print(x)
print(type(x))

# None evaluates to False in a boolean context.
print(bool(x))
# Functions that do not explicitly return a value return None by default.
def none():
    x = 10
z = none()
print(z)
