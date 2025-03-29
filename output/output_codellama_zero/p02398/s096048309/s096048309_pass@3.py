def divisible_sum(numbers):
    return sum(i for i in range(*numbers) if c % i == 0)