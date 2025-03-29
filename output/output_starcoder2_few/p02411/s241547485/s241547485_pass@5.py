<|quote|><|title|$Original$Python$program|>
import sys
sys.stdin = open('input.txt', 'r')
 
while True:
    m,f,r=list(map(int,input().split()))
    if m==f==r==-1:
        break
    if m==-1 or f==-1 or m+f<30:
        print("F")
    elif m+f<50 and r<50:
        print("D")
    elif m+f<65 or r>=50:
        print("C")
    elif m+f<80:
        print("B")
    else:
        print("A")
</|title|><|/quote|>

<|quote|><|title|$Refactored$version|>
import sys
sys.stdin = open('input.txt', 'r')
 
while True:
    m,f,r=list(map(int,input().split()))
    if m==f==r==-1:
        break
    if (m+f<30 and m!=-1) or f==-1 or m==-1:
        print("F")
    elif m+f<50 and r>=50:
        print("D")
    elif m+f<65 and r>=40:
        print("C")
    elif m+f<80:
        print("B")
    else:
        print("A")
</|title|><|/quote|>