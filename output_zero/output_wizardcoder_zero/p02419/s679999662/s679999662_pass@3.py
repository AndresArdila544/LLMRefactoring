```python
w = input().lower()
s = ""
while True:
    tmp = input().lower()
    if tmp == "end_of_text":
        break
    s += " " + tmp
print(s.split().count(w))