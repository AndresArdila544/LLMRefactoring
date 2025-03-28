n = int(input())
s_list, h_list, c_list, d_list = [], [], [] ,[] 
for _ in range(n):
    m,a = input().split()
    if m == 'S': s_list.append(int(a)-1)
    elif m == 'H': h_list.append(int(a)-1)
    else: c_list.append(int(a)-1

for i in range(13):
    if i not in s_list: print("S %d"%i+1)
for i in range(13):
    if i not in h_list: print("H %d"%i+1)
for i in range(13):
    if i not in c_list: print("C %d"%i+1
for i in range(13):
    if i not in d_list: print("D %d"%i+1)