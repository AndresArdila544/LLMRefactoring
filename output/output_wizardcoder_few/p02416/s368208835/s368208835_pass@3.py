The original program works as intended by taking input strings from the user until they enter '0', then printing their sum. However, it can be further simplified using a while loop to achieve the same functionality and reduce its complexity.

Here's the refactored code:

```python
while True:
    s = input()
    if s != '0':
        print(sum(map(int, s))
    else:
        break
```