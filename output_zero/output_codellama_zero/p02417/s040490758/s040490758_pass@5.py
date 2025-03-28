import string

while True:
    try:
        s += input()
    except:
        break
s = s.lower()
for i in range(string.ascii_lowercase):
    print(chr(i)+" :",s.count(chr(i)))