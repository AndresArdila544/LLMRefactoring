a,op,b = [int(i) for i in input().split()]
if op!='?':
	if op=='+':
		print(a+b)
	elif op=='-':
		print(a-b)
	elif op=='*':
		print(a*b)
	elif op=='/':
		print(a//b)