The given program prints the input integer `z` followed by its digits in reverse order separated by a space. It can be refactored as follows:
```python
z = int(input())
a = list(map(int, input().split()))[::-1]
print(" ".join(str(x) for x in a)
```
This uses list slicing to reverse the order of the elements in `a`, and then joins them into a string with spaces between each element using a generator expression. The `[::-1]` slice notation is used instead of `reverse()` since it has better performance than calling the function.

The resulting code is just two lines, as opposed to four, and avoids creating an unnecessary list object in memory.