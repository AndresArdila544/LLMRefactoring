Here's a more compact version:

while True:
    x = input()
    if x == '0': break
    print(sum(list(map(int, x))))