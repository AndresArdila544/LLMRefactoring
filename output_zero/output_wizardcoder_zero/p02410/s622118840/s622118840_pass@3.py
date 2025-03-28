Here's the refactored code:

```python
from numpy import array, dot

def main():
    try:
        n, m = tuple(int(x) for x in input().split())
        matrix = array([[int(x) for x in input().split()] for _ in range(n)]
        vector = array([int(input()) for _ in range(m)])
    except ValueError:
        print("input error")
    else:
        result = dot(matrix, vector)
        print(*result)

if __name__ == "__main__":
    main()
```