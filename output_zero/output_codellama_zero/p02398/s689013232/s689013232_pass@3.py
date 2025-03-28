def count_divisors(a, b, c):
    count = 0
    for num in range(a, b+1):
        if c % num == 0:
            count += 1
    return count