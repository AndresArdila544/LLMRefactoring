a = int(input())
h, m, s = a // 3600, (a % 3600) // 60, a - (h * 3600 - m * 60)
print(f"{h}:{m}:{s}")