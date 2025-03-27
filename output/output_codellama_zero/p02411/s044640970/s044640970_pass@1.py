while True:
	m, f, r = map(int, input().split())
	if m == -1 and f == -1 and r == -1:
		break
	elif m + f < 30 or (m + f >= 30 and r < 50):
		print("F")
	elif m + f < 50:
		print("D")
	else:
		if m + f >= 80:
			print("A")
		elif m + f >= 65:
			print("B")
		else:
			print("C")