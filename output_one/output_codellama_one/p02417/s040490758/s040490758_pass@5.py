import string
s = ""
while True:
    try:
        s += input()
    except:
        break
s = s.lower()
for c in string.ascii_lowercase:
    print(c + " :", s.count(c))