```python
def print_divisible_by_3(n):
    """
    Function to print all numbers divisible by 3 and their multiples less than or equal to n.

    :param n: int - input number
    :return: None
    """
    for i in range(1, n + 1):
        if i % 3 == 0:
            print(" " + str(i), end="")
        elif i % 10 == 3 and not i % 3 == 0:
            print(" " + str(i // 10 * 10, end="")
    
print_divisible_by_3(int(input())
```