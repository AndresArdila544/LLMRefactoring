Here is the refactored version of the program:

while True:
	a,b=map(int,input().split())
	if a==0 and b==0:
	   break
	for i in range(a):
		print('#'*(i == 0 or i == a-1)*b + '.'.join(['#']*(b-2))+'#' if i != 0 else '#'*b)
	print()