# s_list=[]
while True:
    s = input() #文字列
    if s == "-":
        break
    shuffle = int(input())
    s_list.append("".join([s[i] for i in range(shuffle)]))
for i in range(len(s_list)):
    print(s_list[i])