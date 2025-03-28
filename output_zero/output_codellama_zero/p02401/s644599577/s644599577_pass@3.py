a,op,b=input().split()
a,b=int(a),int(b)
while op!="?":
    if op=="+":
        ans = a+b
    elif op=="-":
        ans = a-b
    elif op=="*":
        ans = a*b
    elif op=="/":
        ans = a//b
    
    print("{}".format(ans))
    
    t+=1
    
    a,op,b=input().split()
    a,b=int(a),int(b)