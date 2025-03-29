Here is a refactored version of your code that has fewer lines and improved readability:
n = int(input())
for i in range(1, n+1):
    if i % 3 == 0 or '3' in str(i):
        print(i, end='')