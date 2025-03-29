# Structured Programming
# if 入力: 30, output is " 3 6 9 12 13 15 18 21 23 24 27 30"
integer = int(input())
cout = []
for n in range(1, integer+1):
    if n % 3 == 0:
        cout.append(n)
    else:
        for i in str(n):
            if i == '3':
                cout.append(n)
                break
cout = [str(x) + " " for x in cout]
print("\n".join(cout))