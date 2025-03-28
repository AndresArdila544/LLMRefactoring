Below is the original code:

sec = int(input())
 
h = sec // 3600
m = (sec % 3600) // 60
s = (sec % 3600) % 60
 
print("{}:{}:{}".format(h, m, s))