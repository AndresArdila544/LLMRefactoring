s = ''
while True:
    try:
        s += input().lower()
    except:
        break
print(*(f'{chr(i)} : {s.count(chr(i))}' for i in range(ord('a'), ord('z')+1)), sep='\n')