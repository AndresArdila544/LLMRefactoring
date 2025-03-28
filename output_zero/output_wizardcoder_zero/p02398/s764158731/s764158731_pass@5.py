```python
def count_divisors(a: int, b: int, c: int) -> int:
    """
    Counts the number of integers between a and b (inclusive), which are divisible by c.

    Args:
        a: The start of the range to check for divisibility.
        b: The end of the range to check for divisibility.
        c: The divisor.

    Returns:
        An integer representing the count of integers between a and b (inclusive) that are divisible by c.
    """
    
    # Ensure inputs are valid and within appropriate range
    if 1 <= a <= 10000 and 1 <= b <= 10000 and 1 <= c <= 10000:
        count = sum(1 for i in range(a, b+1) if i % c == 0)
    else:
        count = None
    
    return count
```