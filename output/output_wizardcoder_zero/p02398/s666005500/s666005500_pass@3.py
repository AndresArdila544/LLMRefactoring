def count_divisors(a, b):
    """Function to count number of divisors of a given integer 'a' between 1 and 'b'"""
    x = 0
    n = a
    
    while True:
        if n <= b:
            if a % n == 0:
                x += 1
            n += 1
        else:
            break
            
    return x

c = int(input())
print(count_divisors(*map(int, input().split()))