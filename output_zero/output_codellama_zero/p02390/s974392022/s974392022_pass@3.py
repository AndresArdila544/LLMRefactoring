x = int(input())
h = x //3600
m = (x- h*3600)//60
s = x-(h*3600+m*60)
print(f"{h}:{m:02d}:{s:02d}")