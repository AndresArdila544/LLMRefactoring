S = int(input())
h = (S // 60) // 60
m = (S // 60) - 60* h
s = S % 60
print(f"{h}:{m}:{s}")
