Here is my proposed solution:

def sort_by(data, index):
    return sorted(data, key=lambda x: x[index])


T = 0
H = 0
n = int(input())
for i in range(n):
    s = input()
    t, h = tuple(s.rstrip().split()), (i % 2) * 3
    s1 = sort_by([t, h], index=0)
    if s1[1][1] == "h":
        H += 3
    else:
        T += 3
print(T, H)