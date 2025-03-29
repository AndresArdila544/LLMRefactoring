This is the refactored Python program:
w = input().lower()
ans=0
while True:
    t=input()
    if t== "END_OF_TEXT": break
    ans += len(t.split()) - 1
print (ans)