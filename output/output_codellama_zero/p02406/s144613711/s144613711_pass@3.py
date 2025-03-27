Here is the refactored version of the original program:
num = int(input())
result=""
for i in range(1,num+1):
    if (i%3==0) | ("3" in str(i)):
        result+=" "+str(i)
print(result)