```python
N, M, L = (int(input()) for _ in range(3))
A = [[int(input()) for i in range(M)] for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(L)
for j in A:
    ans = sum(j[i] * B[i][-1] for i in range(len(A)) if i == L - 1 and print(ans) or print(ans, end=' ')
``` 

Explanation:
The original code initializes two matrices A and B of sizes NxM and LxL respectively. Then it loops through the rows in A and columns in B to compute their dot product.
- The first line unpacks the input into variables N, M and L respectively.
- The second line creates A as a list of lists where each inner list contains integers separated by spaces using map function and range() function.
- The third line creates B as a list of lists where each inner list is generated from input().split() method.
- Then the code loops through each row in A (for i2) and for each row, it loops through all elements of that row (for i3), computes their dot product with corresponding element in B[i3][j] and accumulates sum in ans variable which is then printed if j is equal to L-1 or else print the sum separated by a space.