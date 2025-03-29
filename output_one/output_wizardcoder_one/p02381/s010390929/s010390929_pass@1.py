def calculate_stddev(n):
    A = []
    while n != 0:
        nums = list(map(int, input().split()))
        ave = sum(nums) / len(nums)
        for i in range(len(nums)):
            A.append((ave - nums[i]) ** 2)
        p = math.sqrt(sum(A) / n)
        print("{:.8f}".format(p))
        A.clear()
        n = int(input())
calculate_stddev(int(input())

# The refactored version of the code is provided. It has reduced the lines and improved readability by removing the unnecessary variables, using a single loop for both input and calculation.
```python
import math

def calculate_stddev(n):
    while n != 0:
        nums = list(map(int, input().split()))
        sum_of_squares = sum((num - sum(nums) / n) ** 2 for num in nums)
        p = math.sqrt(sum_of_squares / n)
        print("{:.8f}".format(p))
        n = int(input())
calculate_stddev(int(input())