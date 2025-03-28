Here is my Python code:

    while True:
        a=input()
        if '?' in a:break
        print(int(eval(''.join(a.split()))))