# Refactored Code:
while True:
    a, op, b = input().split()   
    a=int(a)                   
    b= int(b)                   


    if op=="?": # opが"?"の時は終了
        break
    else:

        if op=="+":

            print(a+b)

        elif op=="-":

            print(a-b)

        elif op=="*":

            print(a*b)

        elif op=="/":

            print(a//b)