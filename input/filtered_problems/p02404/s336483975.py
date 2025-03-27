while True:
	a,b=map(int,input().split())
	if a==0 and b==0:
	   break
	for i in range(a):
		if i==0 or i==a-1:
			for n in range(b):
				print('#',end='')
		else:
			print('#',end='')
			for g in range(b-2):
				print('.',end='')
			print('#',end='')
		print()
	print()
