```python
a, b, c = map(int, input().split())
count = sum(c % i == 0 for i in range(1, min(a, b) + 1))
print(count)
``` 

Explanation:
We initialize a, b, and c as integers from the given input and then use list comprehension to count the number of factors of c that are less than or equal to b. We calculate the minimum value between a and b for the range function to work properly.
```python
a = int(input())
b = int(input())
c = int(input())
count = sum(c % i == 0 for i in range(1, min(a, b) + 1))
print(count)
```