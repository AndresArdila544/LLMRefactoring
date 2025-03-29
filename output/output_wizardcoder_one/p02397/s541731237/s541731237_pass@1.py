a=[]
while True:
 n=input()
 if n=='0 0':break
 x,y=map(int,n.split())
 if x<y:print(x,' ',y)
 else:print(n)

The refactored version of the code is:
a=[]
while True:
 n=input()
 x,y=map(int,n.split())
 if x>y:print(y,' ',x)