s = ""
while True:
    try:
        s += input().lower()
    except:
        break
for c in range(ord("a"), ord("z") + 1):
    print(chr(c) + " :", s.count(chr(c)))