def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer))

def sub(a, b):
    answer = a - b
    print(str(a) + "-" + str(b) + " = " + str(answer))

def mul(a, b):
    answer = a * b
    print(str(a) + "*" + str(b) + " = " + str(answer))

def div(a, b):
    answer = a / b
    print(str(a) + "/" + str(b) + " = " + str(answer))


still = ""
val1 = int(input("input the first value: "))
val2 = int(input("input the 2nd value: "))
todo = input("What do you want to do \nadd\nsub\nmul\ndiv\ne to exit\n")

while  todo != "e":
    
    if todo == "add":
        add(val1, val2)
 
    elif todo == "sub":
        sub(val1, val2)
        
    elif todo == "mul":
        mul(val1, val2)  
    elif todo == "div":
        div(val1, val2)    
        
    elif todo == "e":
        break
    else:
        print("invalid input")
        todo = input("What do you want to do \nadd\nsub\nmul\ndiv\ne to exit\n")

