```python
def calculate_sum(expr):
    while True:
        try:
            return sum([int(s) for s in expr if s.isdigit()])
        except ValueError:
            break


print(calculate_sum(input()))