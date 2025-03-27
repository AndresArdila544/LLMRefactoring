Here is the refactored version of the program:

s_list = []
while True:
    s = input()
    if s == "-":
        break
    shuffle = int(input())
    for i in range(shuffle):
        h=int(input())
        s = s[h:]+s[:h]
    s_list.append(s)
for s in s_list:
    print(s)