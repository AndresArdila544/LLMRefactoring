list=[]
while True:
    try:
        list.append(input().lower())
    except EOFError:
        break
for c in 'abcdefghijklmnopqrstuvwxyz':
    print(c,":", w.count(c))