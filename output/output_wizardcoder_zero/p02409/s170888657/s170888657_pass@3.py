data = [[0]*10 for _ in range(4)] # Using a list comprehension to create a 2-dimensional array of zeros with a single line
count = int(input())
for i in range(count):
    b, f, r, v = map(int, input().split())
    data[b-1][f-1] += v # Incrementing the value at the given row and column of the array
for row in data:
    print(' '.join([str(col) for col in row])
print('#'*20 if i < 3 else '', end='') # Printing the array, adding a separator after each row except the last one.