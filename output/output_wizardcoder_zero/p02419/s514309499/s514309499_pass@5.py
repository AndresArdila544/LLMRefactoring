W = input()
count = 0
while True:
    T = input().lower()
    if T == "END_OF_TEXT":
        break
    elif W in T.split():
        count += 1
print(count)