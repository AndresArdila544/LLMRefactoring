import sys
input_string = sys.stdin.readline()
x = input_string.split(" ")
sum=0
max=int(x[0])
min=int(x[0])
for i in range(0, int(len(x))):
    sum=sum+int(x[i])
    if max<int(x[i]):
        max=int(x[i])
    elif int(x[i])<min:
        min=int(x[i])
print(str(min)+" "+str(max)+" "+str(sum))