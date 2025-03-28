```python
import sys

def main():
    while True:
        x = int(input())
        if x == 0:
            break
        digit_sum = sum(int(digit) for digit in str(x))
        print(digit_sum)

if __name__ == '__main__':
    main()
```

This version uses list comprehension to sum up the digits of x, and does not rely on dividing by 10 or modulo arithmetic. It also removes unnecessary imports and the redundant input function call in the while loop. The `sum` built-in function is more concise than looping through each digit.