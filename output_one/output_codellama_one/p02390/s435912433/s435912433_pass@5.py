a = int(input())
h, m, s = a // 3600, (a % 3600) // 60, (a % 3600) % 60
print(f"{h:02d}:{m:02d}:{s:02d}")