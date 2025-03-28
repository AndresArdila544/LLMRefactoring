# Refactored version of the code:
n = int(input())
T = 0
H = 0
for s in map(str.rstrip, input() for _ in range(n)):
    s = s.split()
    if s[0] == s[1]:
        T += 1
        H += 1
    else:
        S = [t := (s[0], "t"), h := (s[1], "h")].sort()
        if t[1] == "t":
            T += 3
        elif t[1] == "h":
            H += 3
print(T, H)