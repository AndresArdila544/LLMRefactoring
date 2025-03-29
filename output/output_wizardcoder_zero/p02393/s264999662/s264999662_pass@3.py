```python
a,b,c = map(int, input().split()) # refactored code without using if-else statements and improved readability
print(*sorted([a,b,c]))  # sorting the list of numbers in ascending order using * for unpacking
```