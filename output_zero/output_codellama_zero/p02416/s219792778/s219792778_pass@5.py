def calc_sum(n):
    return sum([int(x) for x in str(n)])
while True:
    n = int(input())
    if n== 0:
        break
    print(calc_sum(n))