while True:
    a,b=map(int, input().split())
    if a==0 and b==0:
        break
    else:
        even, odd = ".", "#"
        for i in range(a):
            print("." * (i%2) + "#" * ((b-1)//2) + "."*(a-(i%2)) + "#" * ((b+1)//2)) if i%2 else "#" * (b) + "." * (a-b)
"""