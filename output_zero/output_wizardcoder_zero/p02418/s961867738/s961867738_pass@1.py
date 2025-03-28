s = input()
p = input()
flag = False
for i in range(len(s)):
    flag = True
    for j in range(len(p)):
        if p[j] == s[(i + j) % len(s)]:
            continue
        else:
            flag = False
            break
    if flag:
        print("Yes")
        break
else:
    print("No")