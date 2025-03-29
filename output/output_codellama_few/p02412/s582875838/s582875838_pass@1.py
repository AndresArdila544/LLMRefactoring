Here is a refactored version of the original Python program:

while True:
    n, x = map(int, input().split())
    if not n + x == 0:
        ans = sum(i * (n - i) for i in range(1, x + 1))
        print(ans)

The refactored version uses a generator expression to calculate the sum of the product of all pairs of integers from 1 to n, and then prints the result. The original code is reduced to two lines, and the complexity of the code is improved by using a more concise method.