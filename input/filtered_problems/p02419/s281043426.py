import sys

W = input()

T = sys.stdin.read()
#T = input()
#f = open("C:\\users\\inago\\desktop\\test.txt", mode="r")
#T = f.read()

T_word = T.split()
#print(T_word)

count = 0
for s in T_word:
    if s == "END_OF_TEXT":
        break
    
    target = s.lower()

    #print("count:%d,  target, W: %s, %s" % (count, target, W))
    if target == W:
        count += 1

print(count)

        

