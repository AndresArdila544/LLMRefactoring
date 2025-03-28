lst1 = []
lst2 = []
answer = 0
n, m = map(int, input().split())
for i in range(n):
    lst1.append(list(map(int, input().split()))
for j in range(m):
    lst2.append(int(input())
for u in range(n):
    answer += sum(lst1[u]) * lst2[j] for j in range(len(lst1[u]))
print(sum(answer))