```python
I = input()
O = ""
list_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in I:
    if i in list_upper:
        O += i.lower()
    else:
        O += i.upper()
print(O)
```