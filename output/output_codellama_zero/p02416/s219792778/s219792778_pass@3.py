Here's a refactored version of your Python program:

def calc_sum(n):
    return sum(map(int, str(n)))

while True:
    n = int(input())
    if n == 0:
        break
    print(calc_sum(n))