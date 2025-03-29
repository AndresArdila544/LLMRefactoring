Here is a rewritten version of your Python program that is more concise and easier to read:
```
a = int(input())
for x in range(1, a + 1):
    if x % 3 == 0 or "3" in str(x):
        print(" {}".format(x), end="")
```