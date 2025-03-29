```python
numbers = list(map(int, input().split()))
sum_of_nums = sum(numbers)
max_num = max(numbers)
min_num = min(numbers)
print("{} {} {} {}".format(min_num, max_num, sum_of_nums))