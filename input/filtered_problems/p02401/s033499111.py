while 1:
	a, op, b = map(str, raw_input().split())
	a = int(a)
	b = int(b)
	if op == "+":
		print a+b
	if op == "-":
		print a-b
	if op == "*":
		print a*b
	if op == "/":
		print a/b
	if op == "?":
		break