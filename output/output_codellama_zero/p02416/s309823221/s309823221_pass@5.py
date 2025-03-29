Here is a refactored version of the code with fewer lines and improved readability:
```
import sys

def main():
    while True:
        x = int(input())
        if not x:
            break
        
        digit_sum = sum(int(c) for c in str(x))
        print(digit_sum)

if __name__ == '__main__':
    main()
```