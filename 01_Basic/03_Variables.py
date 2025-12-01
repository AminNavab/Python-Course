# int
x = 10
print(x)
print(type(x))

# str
x_1 = "abcde"
x_2 = 'abcde'
print(x_1, x_2, sep=" - ")
print(type(x_1), type(x_2),sep=" - ")

# float - duoble
x_3 = 1.10
print(x_3)
print(type(x_3))

# bool
x_4 = False
x_5 = True
print(x_4, x_5, sep=" - ")
print(type(x_4),type(x_5), sep=" - ")
#--------------------------------------------
# type casting
a = int(5)
a_1 = str(5)
a_2 = float(5)
print(a, a_1, a_2, sep=" - ")
print(type(a), type(a_1), type(a_2), sep=" - ")
#----------------------------------------------------
# Camel Case: myVariableName = "John"
# Pascal Case: MyVariableName = "John"
# Snake Case: my_variable_name = "John"
#-----------------------------------------------------
w, z, y = 1,2,3
print(w,z,y,sep=" - ")
w_1= z_1= y_1 = 4
print(w_1,z_1,y_1,sep=" , ")
q = ["w","z","y"]
w_2,z_2,y_2 = q
print(w_2,z_2,y_2,sep=" _ ")
#--------------------------------------------------
n = "python"
m = "is better"
p = 5
print(n,m)
print(n+m)
print(n,m,p)
# print(n+m+p)  => error
#-----------------------------------------
# Global variable
# (1):
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
# (2):Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
#                            To create a global variable inside a function, you can use the global keyword.
x = "awesome"

def myfunc():
  global x
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)



