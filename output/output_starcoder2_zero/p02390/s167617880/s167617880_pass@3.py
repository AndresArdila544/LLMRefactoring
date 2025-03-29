The following Python program works as intended:

S = int(input())
h = (S // 60) // 60
m = (S // 60) - h * 60
s = S % 60
print(f"{h}:{m}:{s}")