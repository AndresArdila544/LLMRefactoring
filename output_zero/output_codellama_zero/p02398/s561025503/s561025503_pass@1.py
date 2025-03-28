def get_num_of_divisors(x):
    a, b, c = x.split()
    return len([i for i in range(int(a), int(b) + 1) if int(c) % i == 0])