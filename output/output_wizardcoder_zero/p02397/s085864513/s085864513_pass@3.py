a = lambda x: map(int,x.split()) if a != [0,0] else break
print(" ".join([str(i) for i in sorted(list(filter(None,input().split()))])