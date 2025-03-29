T = H = 0
n = int(input())
for i in range(n):
    s = input().rstrip().split()
    T += sum([1 for word in s if s[0] == word]) * 2 + 3*(s[0][-1] != s[1][-1])
    H += sum([1 for word in s if s[0][-1] == 't' and word[-1] != 't']) + sum([1 for word in s if s[0][-1] == 'h' and word[-1] != 'h'])/2
print(T, H)