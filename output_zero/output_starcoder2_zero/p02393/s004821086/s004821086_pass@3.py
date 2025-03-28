<|start_of_text|><!---End of text data-->
a,b,c=map(int,input().split())
if a > b :
    tmp = a
    a=b 
    b=tmp
elif b > c:
    tmp=b
    b=c 
    c=tmp
else:
    tmp=a
    a=b 
    b=tmp
print(a,b,c)