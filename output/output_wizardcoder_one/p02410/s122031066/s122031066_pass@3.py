lst1 = []
lst2 = []
for _ in range(int(input())):
    lst1.append([int(x) for x in input().split()])
lst2 = [int(input()) for i in range(len(lst1[0]))]
print(*map(sum, zip(*lst1)), end=" ")
for t in range(m):
    bi=int(input())
    lst2.append(bi)