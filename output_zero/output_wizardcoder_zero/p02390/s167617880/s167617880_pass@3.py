h, m, s = divmod(S, 36000)
print(f"{h//10:d}:{(h%10)*10:{m//10:02d}:{s//10:02d}")