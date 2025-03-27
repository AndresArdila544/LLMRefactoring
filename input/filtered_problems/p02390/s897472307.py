a = input()
h = int(int(a) / 3600)
m = int((int(a)-h * 3600)/60)
s = int((int(a)-h*3600)%60)

print(str(h)+':'+str(m)+':'+str(s))
