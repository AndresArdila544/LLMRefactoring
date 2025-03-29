n=int(input())
 cards=[(m,int(n)) for m,n in input().split()]
 for m in ['S','H','C','D']:
     for n in range(1,13+1):
         if (m,n) not in cards:
             print(m,n)