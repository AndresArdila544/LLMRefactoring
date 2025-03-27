def getInput():
    return [int(x) for x in input().split()]

while True:
    a, b = getInput()
    if not (a == b and a == 0):
        break

for a, b in sorted([a, b] for a, b in map(getInput(), range(2))):
    print(a, b)