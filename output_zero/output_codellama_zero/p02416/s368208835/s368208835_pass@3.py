Here is a refactored version of the original code that has fewer lines and improved readability:

while True:
    s = input()
    if s == '0': break
    print(sum(map(int, s)))