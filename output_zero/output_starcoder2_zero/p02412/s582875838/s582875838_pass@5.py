<|start_of_text|>=
import sys


def gcd(a: int, b: int) -> int:
    while b > 0:
        a, b = b, a % b

    return a


def lcm(a: int, b: int) -> int:
    return (a * b) // gcd(a, b)


while True:
    n, x = map(int, input().split())

    if n + x == 0:
        break

    ans = 0

    for i in range(1, n):
        for j in range(i + 1, n):
            m = lcm(i, j)

            if m < (x - i - j) <= n and lcm(m, min(max(j, x - m), max(i, x - i - j))) == m:
                ans += 1

    print(ans)