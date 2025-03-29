s = ""
while True:
    try:
        s += input()
    except:
        break
s = s.lower()
for i in range(97, 123):
    print(chr(i) + " :", s.count(chr(i)))