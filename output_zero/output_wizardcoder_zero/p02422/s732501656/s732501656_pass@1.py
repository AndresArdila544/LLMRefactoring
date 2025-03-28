```python
def method_processor(str, q):
    for _ in range(q):
        operation, a, b = input().split()
        if operation == "print":
            print(str[int(a) : int(b)+1])
        elif operation == "reverse":
            str = f"{str[:int(a)}{str[int(a):int(b)+1][::-1]}{str[int(b)+1:]}
        elif operation == "replace":
            pre, after = str[:int(a)], str[int(b)+1:]
            str = f"{pre}"+"".join(p)+after
```