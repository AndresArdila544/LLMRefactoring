a, b = map(int, input().split())
for i in range(a):
    bs[i].append(sum(map(int, input().split()))
bs.append([sum(map(int, input().split()) for _ in range(b)])
print(*(" ".join(str(i) for sublist in bs for i in sublist))