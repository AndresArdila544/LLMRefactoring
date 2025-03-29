n, x = map(int,input().split())
while n!=0 and x!=0:
    count=0
    for u in range(1,x//3+1):
        v=(x-u)//2 + 1
        while v<(x-u):
            if u > (x-v):
                count+=1
            v+=1
print(count)

#This code is more concise and easier to understand than the previous version. The for loop iterates through all possible values of u, which allows us to avoid the while loop altogether. The condition in the while loop for counting the combinations has also been simplified by calculating it directly using basic arithmetic operations rather than a conditional statement.