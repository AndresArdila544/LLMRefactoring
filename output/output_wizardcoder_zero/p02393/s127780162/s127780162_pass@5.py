```python
x = list(map(int, input().split())) # convert string input to a list of integers using map and split method
a, b, c = sorted(x) # sort the list of integers and unpack into variables a,b,c
print(*sorted(x)) # print sorted values separated by spaces