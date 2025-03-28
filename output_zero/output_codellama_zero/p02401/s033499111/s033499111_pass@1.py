The original program has been refactored below:

while True:
	try:
		a, op, b = map(str, raw_input().split())
		a = int(a)
		b = int(b)
	except ValueError:
		break

	if op == "+":
		print a+b
	elif op == "-":
		print a-b
	elif op == "*":
		print a*b
	elif op == "/":
		print a/b
	else:
		break