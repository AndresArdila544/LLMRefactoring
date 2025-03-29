def calculate_sum(num):
    total = sum(int(digit) for digit in str(num))
    return total

while True:
    num = int(input())
    if num == 0:
        break
    print(calculate_sum(num))