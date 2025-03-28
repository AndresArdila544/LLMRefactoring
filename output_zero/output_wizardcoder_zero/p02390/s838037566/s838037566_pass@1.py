h, m, s = divmod(S, 360*60)
h //= 60
m //= 60
print(f"{h}:{m}:{s}")