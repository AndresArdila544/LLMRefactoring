#Refactored Version

str = list(input())
num = int(input())
for num in range(num):
	ord = input().split()
	start = int(ord[1])
	end = int(ord[2]) + 1
	if ord[0] == 'replace':
		rep = list(ord[3])
		str[start:end] = rep
	elif ord[0] == 'reverse':
		str[start:end] = str[start:end][::-1]
	else:
		print(''.join(str[start:end]))