```python
buildings = [[[0]*10 for _ in range(3)] for _ in range(4)] # Use list comprehension to initialize buildings and reduce number of lines
informations=int(input())
for i in range(informations):
    information = [int(x) for x in input().split()]
    buildings[information[0]-1][information[1]-1][information[2]-1]+=information[3] # Improve readability and reduce lines by using list comprehension to input integers directly
for i in range(4):
    for j in range(3):
        write(' '.join([str(x) for x in buildings[i][j]]) + ' \n') # Use join() function instead of multiple sys.stdout.write()
    if i != 3:
        print('#'*20)
```