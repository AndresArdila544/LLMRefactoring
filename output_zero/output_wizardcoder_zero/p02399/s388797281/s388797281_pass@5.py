a, b = map(int, input().split())
print("{:<4} {:>10} {:.20f}".format(a // b, a % b, a / b))