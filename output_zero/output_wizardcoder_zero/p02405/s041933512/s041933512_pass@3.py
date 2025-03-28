H,W = map(int, input().split())
print('#'*W if (i+j)%2 else '.' for i in range(H) for j in range(W))