Here's a refactored version of the code:

```python
while True:
    H, W = map(int, input().split())
    
    if H == 0 and W == 0:
        break
    
    print('#' * (W // 2) + '.' * ((W + 1) % 2) + '#' * (W // 2)) * H
```

Explanation:
We can reduce the complexity and lines of code by using string multiplication. 
The inner loop is not necessary as we only need to print half the pattern for each row, so we can use integer division instead of modulo to determine if it's an even or odd row number. Then we concatenate strings with '#' for the top half and '.' for the bottom half using string multiplication. Finally, we print a newline after each row.

```python
H, W = map(int, input().split())
if H == 0 and W == 0:
    break

print('#' * (W // 2) + '.' * ((W + 1) % 2) + '#' * (W // 2)) * H
```

This will print a diamond pattern with '#' in the top half and '.' in the bottom half for odd W values, and alternating '#'s and dots for even W values. The pattern repeats for each row until H=0 and W=0 are entered.