```
while True:
	H, W = list(map(int, input().split()))
	if H == 0 and W == 0:
		break
	print("#" * W for _ in range(H))
```