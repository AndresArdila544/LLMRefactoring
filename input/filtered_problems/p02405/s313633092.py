while True:
    a,b=map(int, input().split())
    if a==0 and b==0:
        break
    else:
        b_even=""
        b_odd=""
        for j in range(b):
            if j%2==0:
                b_even=b_even+"."
            else:
                b_even=b_even+"#"
                
        for j in range(b):
            if j%2==0:
                b_odd=b_odd+"#"
            else:
                b_odd=b_odd+"."
        
        for i in range(a):
            if i%2==0:
                print(b_odd)
            else:
                print(b_even)
        print("")
