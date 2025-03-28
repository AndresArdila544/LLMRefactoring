while True:
	m, f, r = map(int, input().split())
	if m == -1 and f == -1 and r == -1:
		break
	if m == -1 or f == -1:
		print("F")
	elif m + f >= 80:
		print("A")
	else:
		grade = "B" if m + f >= 65 else "C" if m + f >= 50 and r >= 50 else "D"
		print(grade)