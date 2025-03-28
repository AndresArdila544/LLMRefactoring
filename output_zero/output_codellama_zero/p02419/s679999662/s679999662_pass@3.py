```
input_list = []
while True:
    tmp = input()
    if tmp == "END_OF_TEXT":
        break
    input_list.extend(tmp.lower().split())
    
print(input_list.count(w))
```