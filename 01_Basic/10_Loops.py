# (1): While loop
x = 5
while x>1:
    print(x) 
    x -= 1

i = 0
while i < 6:
    i += 1
    if i == 3:
       continue
    print(i)
z =10
while z>1:
    if z == 6:
        print(z)
        break
    z -= 1
## The else Statement: With the else statement we can run a block of code once when the condition no longer is true.
j = 1
while j < 6:
  print(i)
  j += 1
else:
  print("j is no longer less than 6")
print("====================")
# (2): for loop => A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
num = [1,2,3,4,5,6]
for i in num:
   print(i)

for i in num:
   print(i)
   if i == 3:
      continue
   
for i in num:
   print(i)
   if i == 3:
      break
# Else in For Loop: The else keyword in a for loop specifies a block of code to be executed when the loop is finished.
# If the loop breaks, the else block is not executed
for x in range(6):
  print(x)
else:
  print("Finally finished!")
# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for i in num:
   pass
