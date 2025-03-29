n = int(input())
for i in range(n):
    point_t += 3 if input().split()[0] > input().split()[1] else 0
    point_h += 3 if input().split()[0] < input().split()[1] else 0
    point_t += 1 if input().split()[0] == input().split()[1] else 0
    point_h += 1 if input().split()[0] == input().split()[1] else 0
print(point_t, point_h)