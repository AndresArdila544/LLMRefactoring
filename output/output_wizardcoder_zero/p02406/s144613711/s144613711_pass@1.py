num = int(input())
result=""
for i in range(1, num+1):
    if not i%3 and str(i).find("3") == -1:
        result += " "+str(i)
print(result)