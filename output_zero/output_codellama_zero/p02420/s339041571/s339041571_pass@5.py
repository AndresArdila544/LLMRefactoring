while True:
    line = input()
    if line=='-':  break
    h = int(input())
    print(line[h:] + line[:h])