Here's the refactored version of the code:

```python
while True:
    s = input()
    if s == "-":
        break
    shuffle = int(input())
    for _ in range(shuffle):
        h = int(input())
        s = s[h:] + s[:h]
    print(s)
```

The original code appends each modified string to a list `s_list`, then prints the elements of that list in order. However, it does not modify any other variables or strings in the input. Therefore, you can simplify the code by removing `s_list` entirely and just printing the modified string after each shuffle operation.