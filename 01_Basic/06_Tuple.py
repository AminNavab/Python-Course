# tuple_name = (.................)
"""Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets."""
"""NOTE:
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members."""
# create tuple
## (1):
num = (1,2,3,4,5,6,7,8,9)
name = ("a","b","c")
x = (True, False, True)
z = (1,2,1.10,"a",True)
## (2):
num1 = tuple((1,2,3,4,5,6))
print(num)
print(type(num))
print(num1)
print(type(num1))
print(z)
print(type(z))
## this not a tuple!!!!
name1 = ("a")
print(type(name1))
## but this is a tuple??
name2 = ("a",)
print(type(name2))

#---------------------------------
# len:
print(len(num))
#---------------------------------
# Access:
print(num[0])
print(num[-1])
print(num[2:6])
print(num[3:])
print(num[:7])
if 3 in num:
    print("3 is in num")
#--------------------------------
# Change: tuple can not change
# tuple -> list -> change -> tuple
x = list(num)
x[-1] = 99
x[5] = 66
num = tuple(x)
print(num)
#--------------------------------
# add: tuple can not add
# tuple -> list -> change -> tuple
z = list(num)
z.append(10)
z.insert(10,11)
z.insert(0,0)
num = tuple(z)
print(num)
w = (12,)
num +=w
print(num)
#----------------------------------------
# remove: tuple can not remove
# tuple -> list -> change -> tuple
q = list(num)
q.remove(7)
num = tuple(q)
print(num)
#--------------------------------------
# Unpacking:
c = (1,2,3)
(a,b,c1) = c
print(a)
print(b)
print(c1)
#--------------------------------------
# Using Asterisk*: If the number of variables is less than the number of values,
#                   you can add an * to the variable name and the values will be assigned to the variable as a list.
m = (1,2,3,4,5,6,7,8,9)
(f,g,*h) = m 
print(f)
print(g)
print(h)
# If the asterisk is added to another variable name than the last,
# #            Python will assign values to the variable until the number of values left matches the number of variables left.
m = (1,2,3,4,5,6,7,8,9)
(f,*g,h) = m 
print(f)
print(g)
print(h)
#----------------------------------
# Loop:
x = ("a","b","c")
for i in x:
    print(i)
for i in range(len(x)):
    print(x[i])
#------------------------------------
# Join tuple:
b = (1,2,3)
d = (4,5,6)
e = b+d
print(e)
f = b*2
print(f)
#-------------------------------------
# Method:
## count(): The count() method returns the number of times a specified value appears in the tuple.
k = (1,2,3,4,5,2,1,4,8,2,6,4,8,6,2,1)
print(k.count(2))
## index(): The index() method finds the first occurrence of the specified value.
#           The index() method raises an exception if the value is not found.
print(k.index(6))



