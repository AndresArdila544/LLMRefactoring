s = int(input())

h = s // 3600
s = s - 3600 * h
m = s // 60
s = s - 60 * m

print(h,':',m,':',s,sep='')
