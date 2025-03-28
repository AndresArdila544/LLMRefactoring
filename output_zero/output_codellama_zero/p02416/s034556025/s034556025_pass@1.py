Here is the refactored Python program:

while True:
    num = input()
    if(num == "0"): break
    print(sum(int(i) for i in num))