h, m, s = divmod(int(S), 360)
print(f"{h//1:%02d}:{(m+s)//60%60:02d}:{s%60:02d}")

Example:
If the input is "540", then the output will be "09:00:00".