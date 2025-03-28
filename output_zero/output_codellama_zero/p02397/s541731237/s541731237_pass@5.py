a=[]
while True:
 n=input()
 if n=='0 0':break
 x,y=map(int,n.split())
 print(x>y and y,' ',x) or n