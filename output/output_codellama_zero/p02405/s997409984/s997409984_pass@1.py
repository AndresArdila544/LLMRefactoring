def f(a, b):
    if a == 0: break
    k = b // 2
    if i % 2 == 0: #偶数
        print("#." * k) if b % 2 == 0 else print("#." * (k) + "#")
    else: #奇数
        print(".#" * k) if b % 2 == 0 else print(".#" * (k) + ".")

L = []
while True:
    a, b = map(int, input().split())
    L.append([a, b])
    if a == 0 and b == 0:
        break