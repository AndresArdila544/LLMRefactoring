Here is the modified program:
while True:
    a, op, b = input().split()   # 1 line change
    a=int(a)
    b=int(b)

    if op=="?":
        break                     # 1 line change
    elif op in ("+", "-", "*", "/"): # use the "in" operator to check multiple possible values of "op"  
        print(eval(f"{a} {op} {b}"))

Explanation:
The first improvement is reducing the number of lines by combining two lines into one using the "=" operator. The second change is using the "in" operator to check multiple possible values of "op". This makes the code more concise and easier to read.