### The goal of this task is to improve the Python program's logic by making it more readable while keeping its functionality as-is. 


# Original code with 10 lines:
while True:
    x = input()
    if x == '0':
        break
    else:
        x_list = list(map(int, x))
        goukei = sum(x_list)
        print(goukei)
        

# Refactored code with 5 lines:
while True:
    x = input()
    if x == '0': break
    else:
        x_list = list(map(int, x))
        goukei = sum(x_list)
        print(goukei)