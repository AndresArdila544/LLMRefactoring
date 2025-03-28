My refactored solution:

w = input()

s = []
while True:
    tmp = input().lower()
    if tmp == "END_OF_TEXT":
        break
    s += tmp.split()
print(s.count(w))