Here is a refactored version of the code with fewer lines and improved readability:

I=input()
a,b = map(int, I.split())
print("a < b" if a<b else "a > b" if a>b else "a == b")