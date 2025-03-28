def f(a, b):
    for i in range(a):
        k = b // 2
        if i % 2 == 0: # 偶数
            print("#." * k + ("#" if b % 2 else ""))
        else: # 奇数
            print(".#" * k + (".#" if b % 2 else ""))
    print()

while True:
    a, b = map(int, input().split())
    f(a, b)
    if not (a and b): break