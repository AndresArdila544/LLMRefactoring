from math import sqrt

while True:
    try:
        n = int(input())
        if n == 0:
            break
        s = list(map(int, input().split()))
        ans.append(sqrt(sum([(ele - sum(s) / len(s)) ** 2 for ele in s]) / len(s)))
    except ValueError:
        break
for ele in ans:
    print(ele)