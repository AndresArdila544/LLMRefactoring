Here is a cleaner, more concise, and improved version of your Python program:

str = input().split()
num = int(input())
for i in range(num):
	ord = str[i].split()
	start, end = int(ord[1]), int(ord[2])+1
	if ord[0] == 'replace':
		rep = list(ord[3])
		str[start:end] = rep
	elif ord[0] == 'reverse':
		temp = ''.join(str[start:end])
		rev = temp[::-1]
		str[start:end] = rev
	else:
		print(''.join(str[start:end]))