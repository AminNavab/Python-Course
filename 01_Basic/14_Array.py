# NOTE: Python does not have built-in support for Arrays, but Python Lists can be used instead.
# Create:
numbers = [1,2,3,4,5,6,7,8,9]
# Access:
print(numbers[0])
print(numbers[5])
# Len:
print(len(numbers))
# Use Loop:
for i in numbers:
    print(i, end="  ")
print()
# Add element:
numbers.append(10)
numbers.append(11)
for i in numbers:
    print(i, end="  ")
print()
# Delete element:
# (1)
numbers.pop()
numbers.pop(4)
# (2)
numbers.remove(8)
numbers.remove(1)
for i in numbers:
    print(i, end="  ")
print()