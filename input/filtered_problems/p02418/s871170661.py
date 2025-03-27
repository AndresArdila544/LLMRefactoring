string = input()
pattern = input()

string = string * 2
if pattern in string:
    print("Yes")
else:
    print("No")
