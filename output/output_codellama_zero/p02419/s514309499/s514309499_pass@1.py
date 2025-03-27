W = input()
t=[]
while True:
    T=input()
    if T=="END_OF_TEXT":break
    else: t.append(T)
count=0
for i in range(len(t)):
    l=t[i].split()
    for j in range(len(l)):
        l[j]=l[j].lower()
        if l[j]==W:
            count+=1
print(count)