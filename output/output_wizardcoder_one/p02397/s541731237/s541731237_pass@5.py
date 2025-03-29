a=[]
while True:
 n=input()
 if not n:break
 x,y=map(int,n.split())
 a.append([x,y])
 for i in range(len(a)):
  for j in range(i+1,len(a)):
   if a[i][0]<a[j][0]:
    if a[i][1]>a[j][1]:print(a[j],' ',a[i])
    else:print(n)