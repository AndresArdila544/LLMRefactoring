Here's a refactored version of the code that has fewer lines and improved readability:

```python
a = list(map(int, input().split()))
dise_list = [0] * len(a)
for _ in range(len(a)):
    dise_list.append(a[_])
class Dise():
    def __init__(self, a):
        self.dise = dise_list

    def roll(self, dir):
        if "N" in dir:
            self.dise[0], self.dise[1], self.dise[4], self.dise[5] = self.dise[1], self.dise[5], self.dise[0], self.dise[4]
        elif "S" in dir:
            self.dise[0], self.dise[1], self.dise[4], self.dise[5] = self.dise[4], self.dise[0], self.dise[5], self.dise[1]
        elif "E" in dir:
            self.dise[0], self.dise[2], self.dise[3], self.dise[5] = self.dise[3], self.dise[0], self.dise[5], self.dise[2]
        elif "W" in dir:
            self.dise[0], self.dise[2], self.dise[3], self.dise[5] = self.dise[2], self.dise[5], self.dise[0], self.dise[3]
    
    # 確認用
    def output(self):
        print(self.dise[0])
```

We can use list comprehension and the `in` operator to reduce the code in the `__init__()` method, and simplify the input conversion using `map()`. We can also remove the extra variable `pop_str` from `roll()` since it's not needed.