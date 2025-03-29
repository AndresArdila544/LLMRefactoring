```python
def execute(*args):
    return sorted(list(map(int, args))

if __name__ == '__main__':
    numbers = list(map(int, input().split(' ')))
    print(execute(*numbers))
```