```python
I = raw_input()
O=str()
for char in I:
    if char.isupper():
        O += char.lower() 
    else:
        O += char.upper()
print(O)