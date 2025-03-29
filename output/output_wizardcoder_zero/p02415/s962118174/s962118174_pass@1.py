```python
string = input()
for i in string:
    print(i.upper() if i.islower() else i.lower(), end="")  # Toggle case based on whether i is upper or lowercase.
```