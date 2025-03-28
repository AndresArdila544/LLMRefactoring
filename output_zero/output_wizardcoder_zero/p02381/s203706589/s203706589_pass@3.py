n = int(input())
while n != 0:
    l = list(map(int, input().split()))
    m = sum(l) / len(l)
    print(f'{sum((s-m)**2 for s in l) / len(l):.5f}')