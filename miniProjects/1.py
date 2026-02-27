# calculator(mashin hesab) 
def g (a,b):
    result = a+b
    print(f"{a}+{b}={result}")
def m (a,b):
    result = a-b
    print(f"{a}-{b}={result}")
   
def z (a,b):
    result = a*b
    print(f"{a}*{b}={result}")
def t (a,b):
    result = a/b
    print(f"{a}/{b}={result}")

def calculator():
    a = int(input("number1 \n"))
    b = int(input("number2 \n"))
    operator = input("operator \n")
    if operator=="+":
        g (a,b)
    elif operator=="-":
        m (a,b)
    elif operator=="*":
        z (a,b)
    elif operator=="/":
        t (a,b)
    else:
        print("erorr")            

print(calculator())  