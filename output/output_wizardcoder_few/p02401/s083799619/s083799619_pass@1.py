refactored_code = """
while True:
    a=input()
    if '?' in a:break
    print(int(''.join([str(eval(x) for x in a.split()]))
"""