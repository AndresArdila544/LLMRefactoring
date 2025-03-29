```python
import math

def main():
    a = input()
    table = list(map(int, input().split()))
    print(min(table), max(table), sum(table))

if __name__ == '__main__':
    main()