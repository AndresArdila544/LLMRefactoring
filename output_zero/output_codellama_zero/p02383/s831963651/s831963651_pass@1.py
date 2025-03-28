Here is the refactored version of your original Python program:

a = list(map(int, input().split()))
for d in input():
	b = a[1:] if d == "N" else a[:4] if d == "E" else a[2:] if d == "S" else a[-3:]
	a = b
print(a[0])