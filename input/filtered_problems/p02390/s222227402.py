S = int(input())
H=S//3600
S-=H*3600
M = S//60
S-=M*60
print("{}:{}:{}".format(H,M,S))
