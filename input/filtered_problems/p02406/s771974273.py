n = int(input())
number = []
for i in range(1, n + 1):
	if i % 3 == 0 or str(i).find("3") != -1:
		number.append(i)

answer = "".join(" "+str(j) for j in number)
print(answer)
