def calc_sum(n):
    return sum(int(digit) for digit in str(n)) if n else 0 # If n is non-zero, return the sum of the digits; otherwise, return 0.

while True:
    n = int(input())
    print(calc_sum(n)) 
    if not n:
        break