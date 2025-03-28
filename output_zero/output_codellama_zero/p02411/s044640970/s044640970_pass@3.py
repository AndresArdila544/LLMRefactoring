while True:
	m, f, r = map(int, input().split())
	if (m == -1) and (f == -1): 
		break;
	else if (m + f >= 80):
		print("A")
	elif (m + f >= 65):
		print("B")
	elif (m + f >= 50):
		print("C")
	elif (m + f >= 30) and (r >= 50):
		print("C")
	else:
		print("D")