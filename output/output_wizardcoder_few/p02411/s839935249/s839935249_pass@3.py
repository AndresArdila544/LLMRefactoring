```python
while True:
    m, f, r = map(int, input().split())
    if (m == f == r == -1):
        break
    result = ["F" if m < 0 or f < 0 else "A" if m + f >= 80 else "B" if m + f >= 65 else "C" if m + f >= 50 and r >= 50 else "D" for i in range(1)]
    print(*result)
```

Explanation:
- We can use a list comprehension to replace the conditional statements.
- Instead of appending to the result list, we can directly append the corresponding grade to it based on the condition. If m < 0 or f < 0, then we append "F", else if m + f >= 80, we append "A", etc.
- Since the input is only a single line of integers separated by spaces, we don't need to iterate over a range, but can directly use the first element of the tuple returned by `map(int, input().split())` to get all three values at once. 
- We can also use a single print statement to output each grade in the result list with a space separator.
- Note that we don't need the else statement for "F", as it will be covered by the previous conditions.