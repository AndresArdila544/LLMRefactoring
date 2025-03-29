Here is the refactored version of the program with fewer lines and improved readability:

```python
while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    for i in range(H):
        for j in range(W):
            print("#."[i%2*2:][::-1], end='')
        print()
```
Explanation: 
- We use the ternary operator `i % 2 == 1` to check if i is odd or even. If it's odd, we print ".", otherwise, we print "#".
- The `[i%2*2:]` slice notation returns either an empty string (`""`) or a "." based on the value of `i`.
- We use the `[::-1]` step to reverse the resulting string, so that odd lines are printed with "." and even lines are printed with "#". 
- The final output has `H` rows each containing `W` characters.
- We use a nested for loop to iterate over both dimensions of the grid.