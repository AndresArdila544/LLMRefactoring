Here's a refactorized version of the code with fewer lines and improved readability:

```python
def calculate_area_perimeter(a, b):
    return f"{a*b}, {(a+b)*2}"

s = input().split()
print(*map(int, s), sep=",")
print(calculate_area_perimeter(*map(int, s)))