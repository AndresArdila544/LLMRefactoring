def get_number_of_divisors(a, b, c):
    return sum(c % num == 0 for num in range(a, b+1))