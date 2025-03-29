```python
nums = input().split()
a, b, c = int(nums[0]), int(nums[1]), int(nums[2])
print('Yes' if a < min(b, c) and b > max(a, c) else 'No')
```