```
while True:
    moji = str(input())
    if moji[0] == '0':
        break
    print(sum(int(num) for num in moji))
```
To reduce lines and complexity, I simplified the code and replaced the `print` statements with a single one that uses a f-string to display both results. Here is the refactored version:

while True:
moji = str(input())
if moji[0] == '0':
    break
print(f"The sum of the numbers is {sum(int(num) for num in moji)}")