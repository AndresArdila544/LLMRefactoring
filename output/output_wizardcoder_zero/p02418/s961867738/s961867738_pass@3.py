s = input()
p = input()

for i in range(len(s)):
    if s[(i+j) % len(s)] == p[j] for j in range(len(p)):
        print("Yes")
        break
else:
    print("No")