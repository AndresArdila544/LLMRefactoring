```python
l = list(map(int, input().split()))
print(l[0]*l[1], 2*(l[0]+l[1]))
```
```python
list(map(lambda x: print(x), l)) # prints each element of the list "l" 
```

```python
result = lambda x, y: x*y
print(result(l[0]*2, l[1]+l[0]) # multiplies the first element by 2 and adds it to the second element 
```

```python
result = list(map(lambda x: x * 2 if i % 2 == 0 else x+x, range(len(l))) # doubles even numbers in l and adds them to themselves 
print(sum(result))
```