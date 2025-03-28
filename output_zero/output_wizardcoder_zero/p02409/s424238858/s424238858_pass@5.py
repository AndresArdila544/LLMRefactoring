rooms = [[[0]*10 for _ in range(3)] for _ in range(4)]
for _ in range(int(input())):
    a,b,c = map(lambda x: int(x)-1, input().split())
    rooms[a][b-2] += c

for i in zip(*([iter(rooms[:3])]*3):
    print(*i)
    if not (i == rooms[-1] and j != 2):
        print("####################")
"""