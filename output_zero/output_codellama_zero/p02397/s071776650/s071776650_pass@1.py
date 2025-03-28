Here is the refactored version of the code:

li = []
while True:
    a,b = map(int, input().split())
    if a == b and a == 0:
        break
    li.append(sorted([a,b]))
for a,b in li:
    print(a,b)