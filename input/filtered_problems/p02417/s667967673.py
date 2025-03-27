list=[]

try:
    while True:
        list.append(input())
except EOFError:
    pass

for i in range(len(list)):
    list[i]=list[i].lower()
w=''.join(list)

for c in 'abcdefghijklmnopqrstuvwxyz':
    print(c,':',w.count(c))
    


