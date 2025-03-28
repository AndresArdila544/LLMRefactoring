s = raw_input()
p = raw_input()
flag = 0
for i in range(len(s)):
    flag = 1
    for j in range(len(p)):
        if p[j] != s[(i + j) % len(s)]:
            flag = 0
            break
    if flag:
        print "Yes"
        break
else:
    print "No"