a, b, c = map(int, input().split())
s = sum([1 for i in range(1, b+1) if (i != 0) and (c % i == 0 or c % -i == 0)] + [1])