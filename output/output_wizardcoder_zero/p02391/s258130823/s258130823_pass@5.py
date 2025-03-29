s=input().rstrip().split()
print("a > b" if int(s[0])>int(s[1]) else "a < b" if int(s[0])<int(s[1]) else "a == b")