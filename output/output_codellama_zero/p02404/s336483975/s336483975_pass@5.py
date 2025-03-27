def print_pyramid(a, b):
	if a == 0 and b == 0:
		break
	for i in range(a):
		if i == 0 or i == a - 1:
			print('#' * b)
		else:
			print('#' + '.' * (b-2) + '#')