Here is a refactored version of your original code that has fewer lines and improved readability:

str = list(input())
num = int(input())

for ord in range(num):
	ord = input().split()
	start = int(ord[1])
	end = int(ord[2]) + 1

	if ord[0] == 'replace':
		rep = list(ord[3])
		str[start:end] = rep
	elif ord[0] == 'reverse':
		temp = str[start:end]
		rev = temp[::-1]
		str[start:end] = rev
	else:
		print(''.join(str[start:end]))