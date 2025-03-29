def count_divisors(a, b):
    num_divisors = sum([1 for i in range(a,b+1) if c%i == 0])
    return num_divisors
a, b, c = map(int, input().split())
print(count_divisors(a, b))