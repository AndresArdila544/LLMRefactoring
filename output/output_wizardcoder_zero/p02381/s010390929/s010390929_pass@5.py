A=[]
while True:
    n = int(input())
    if n == 0:
        break
       
    else:
        b = list(map(int, input().split()))
        ave = sum(b) / n
        A.extend(((ave - i)**2 for i in b)
        p = math.sqrt(sum(A)/n)
        print("{:.8f}".format(p))
        A.clear()
        
You can reduce the code by using a list comprehension instead of creating an empty list and appending values to it.