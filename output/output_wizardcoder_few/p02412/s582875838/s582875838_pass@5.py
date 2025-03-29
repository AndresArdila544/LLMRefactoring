Refactored version:

while True:
    n = int(input())
    x = int(input())
    if n+x == 0:
        break
    ans = sum([1 for i in range(1,n) for j in range(i+1,n) if j<x-i-j<=n])
print(ans)

Explanation:
We use the built-in function `sum` to iterate over all possible pairs of numbers between 1 and n (excluding n), calculate the condition `j < x - i - j <= n`, and increment a counter for each pair that satisfies it. The loop is nested inside the first loop to ensure that only valid pairs are counted.

We can simplify this further by using list comprehension instead of loops, and calculating the sum at once:

while True:
    n = int(input())
    x = int(input())
    if n+x == 0:
        break
    ans = sum([1 for i in range(1,n) for j in range(i+1,n) if j<x-i-j<=n])
print(ans)

This version is still readable and concise.