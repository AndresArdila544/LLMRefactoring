```python
def main():
    while True:
        a, b = map(int, input().split())
        if not (a and b):
            break
        for i in range(0, a):
            for j in range(0, b):
                print("#", end='')
            print()
    
if __name__ == "__main__":
    main()
```