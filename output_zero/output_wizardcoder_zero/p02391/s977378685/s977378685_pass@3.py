```python
def compare(a, b):
    return "a == b" if a == b else ("a < b" if a < b else "a > b")  

if __name__ == '__main__':
    a,b = map(int, input().split())
    print(compare(a, b))
```