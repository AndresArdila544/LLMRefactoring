The original program takes input of height (h) and width (w), then prints a matrix consisting of "#" characters in rows of height h and columns of width w. The while loop is infinite until user inputs zero for height (h=0), so I have removed the while loop and just added an if statement inside the outer for loop to print new lines after printing all the rows.

```python
n,w = map(int,input().split())
for i in range(n):
    for j in range(w):
        print("#",end="")
    print()
```