num = int(input())
result=""
for i in range(1,num+1):
    if i%3==0:
        result+=" "+str(i)
    elif str(i).find("3")!=-1:
        result+=" "+str(i)
print(result)

