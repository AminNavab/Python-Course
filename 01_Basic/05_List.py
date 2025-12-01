"""
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets"""
# create a list:
# (1):
num = [1,2,3,4,5,6,7,8,9]
# (2):The list() Constructor It is also possible to use the list() constructor when creating a new list.
newnum = list((11,"22",33,44.0,55,'66',77,88.0,99))
newnum2 = list(num)
# accese:
print(num)
print(newnum)
print(num[0])
print(num[5])
## Negative Indexing: Negative indexing means start from the end
print(num[-1])
print(num[-3])
## Range of Negative Indexes
print(num[2:7])
print(num[:7])
print(num[6:])
print(num[-7:-3])
#-------------------------------------
# ckeking in list:
if 6 in num:
    print("6 in num")
#-------------------------------------
# change:
num[5] = 12
num[8] = 18
num[1:3] = [111,222]
print(num)
#--------------------------------------
# add to list
## insert: add to index
num.insert(5, "5")
num.insert(11, 1111)
print(num)
## append: add to end 
num.append(444)
num.append("amin")
print(num)
#-------------------------------------
# list len:
print(len(num))
# list type:
print(type(num))
#--------------------------------------
# delete from list
## remove: delete item
num.remove(1)
print(num)
## pop: delete from end
num.pop()
print(num)
## pop(indec): delete from index
num.pop(2)
print(num)
## del keyword:
del num[1]
print(num)
del num[-1]
print(num)
## clear:
num.clear()
print(num)
#-------------------------------------
# Loop list:
x = ["a",2,3.5]
for i in x:
    print(i)

for i in range(len(x)):
    print(x[i])

[print(i) for i in x]
## List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
## syntax: newlist = [expression for item in iterable if condition == True]
x_1 = [i for i in x if i==2]
print(x_1)
x_2 = [x for x in range(1,5)]
print(x_2)
x_3 = [i for i in range(1,20)  if 4<i<8]
print(x_3)
x_4 = [str(x) for x in x]
print(x_4)
x_5 = [x if x != "a" else "A" for x in x]
print(x_5)
x_6 = ["B" for z in x]
print(x_6)
#----------------------------------------------
# Sorting:
a = [1,25,88,45,62,41,55]
b = ["a","d","e","b","c"]
a.sort()
b.sort()
print(a)
print(b)
## Sort Descending
a.sort(reverse=True)
b.sort(reverse=True)
print(a)
print(b)
## Case Insensitive Sort
b = ["a","d","B","e","A","b","c","E"]
b. sort()
print(b)
b.sort(key=str.lower)
print(b)
b.sort(key=str.upper)
print(b)
#-----------------------------------------------
# revers:
z = [1,2,3,4,5,6]
z.reverse()
print(z)
#------------------------------------------------
# copy list:
v = [1,2,3,4,5]
v_1 = v.copy()
print(v_1)
#-------------------------------------------------
# join list:
s = [1,2,3]
s_1 = [4,5,6]
s_2 = s+s_1
print(s_2)
for i in s:
    s_1.append(i)
print(s_1)
s_1.extend(s)
print(s_1)



"""
Method	    Description
append()	Adds an element at the end of the list
clear()  	Removes all the elements from the list
copy()   	Returns a copy of the list
count() 	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index() 	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()   	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()   	Sorts the list
"""