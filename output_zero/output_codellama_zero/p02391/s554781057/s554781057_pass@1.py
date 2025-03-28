Here is a refactored version of the program that has fewer lines and improved readability:

a, b = map(int, input().split())
print(f'{a} {("<" if a < b else ">" if a > b else "=")}{b}')