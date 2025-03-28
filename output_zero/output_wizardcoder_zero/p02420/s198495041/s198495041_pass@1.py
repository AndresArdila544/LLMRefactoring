while True:
    C = input() + '\n'
    if C == "-":
        break
    else:
        m = int(input())
        for i in range(m):
            h = int(input())
            c = input()
            C += c 
print(C.rstrip('\n'))