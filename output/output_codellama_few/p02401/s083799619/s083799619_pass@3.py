import sys
while True:
    try:
        a = sys.stdin.readline().strip()
    except:
        break
    if "?" in a:
        break
    print(eval("".join(a.split())))