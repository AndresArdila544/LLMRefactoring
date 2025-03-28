n = int(input())
listA = [list(map(int, input().split())) for i in range(n)]
building_matrix = [[[0] * 10 for j in range(3) for k in range(4)] for l in range(n)]
for i in listA:
    building_matrix[i[0]-1][i[1]-1][i[2]-1] += i[3]

for floor in building_matrix[:3]:
    print(" ".join(str(room) for room in floor))
print("#" * 20)
for floor in building_matrix[3:]:
    print(" ".join(str(room) for room in floor))