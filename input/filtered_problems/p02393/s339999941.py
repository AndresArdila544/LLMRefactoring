a,b,c=map(int,input().split())

if a>b>c:
  print(c,b,a)

elif a>c>b:
  print(b,c,a)

elif b>a>c:
  print(c,a,b)

elif b>c>a:
  print(a,c,b)

elif c>a>b:
  print(b,a,c)

elif a==b>c:
  print(c,a,b)

elif c==a>b:
  print(b,a,c)

elif b==c>a:
  print(a,b,c)

elif a==b<c:
  print(a,b,c)

elif c==a<b:
  print(c,a,b)

elif b==c<a:
  print(b,c,a)

else:
  print(a,b,c)