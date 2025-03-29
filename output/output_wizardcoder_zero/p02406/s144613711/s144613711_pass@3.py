num = int(input())
result = ""
for i in range(1, num+1):
    if not i%3 and "3" not in str(i):
        result += str(i) + " "
print(result)