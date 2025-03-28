Here is a more concise and readable version of the code:

while True:
    n, x = (int(x) for x in input().split())
    if (n, x) == (0, 0): break
    cnt = sum(comb(i, 3) for i in range(1, n+1) if i + i + i <= x)
    print(cnt)

This version uses the built-in `sum` function to calculate the number of triples that sum up to `x`. It also uses the `comb()` function from the `math` module to calculate the number of combinations of three elements. This reduces the number of lines of code and makes it easier for others to understand the code's logic.