n = int(input())
for _ in range(n):
    x = input()
    if int(x) > 0:
        print(sum([int(x[i] for i in range(len(x))]) if '0' <= x[i] <= '9' else -1)
    else:
        break