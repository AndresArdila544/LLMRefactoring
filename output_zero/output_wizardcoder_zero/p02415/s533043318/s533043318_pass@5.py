```python
s = input()
trans = str.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", "cdefghijklmnopqrstuvwxyzabCDEFGHIJKLMNOPQRSTUVWXYZ")
print(s.translate(trans))