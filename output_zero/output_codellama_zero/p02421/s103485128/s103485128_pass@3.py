Here is a more concise version of the original Python program:

n = int(input())
T = H = 0
for i in range(n):
    s = input().rstrip().split()
    if s[0] == s[1]:
        T += 1
        H += 1
    else:
        t = [s[0], "t"]
        h = [s[1], "h"]
        S = sorted([t, h])
        if S[1][1] == "t":
            T += 3
        elif S[1][1] == "h":
            H += 3
print(T, H)