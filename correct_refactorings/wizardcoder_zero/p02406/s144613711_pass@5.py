num = int(input())
result = ""
for i in range(1, num+1):
    if not (i % 3):
        result += " " + str(i)
    elif "3" in str(i):
        result += " " + str(i)
print(result.strip())