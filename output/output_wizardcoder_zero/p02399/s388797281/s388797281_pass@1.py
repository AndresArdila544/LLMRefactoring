a, b = map(int, input().split())
divisor = a // b
remainder = a % b
quotient = "{:10.20f}".format(a / b)
print(divisor, remainder, quotient)