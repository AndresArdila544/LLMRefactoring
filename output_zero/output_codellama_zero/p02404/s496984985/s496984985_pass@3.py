while True:
 W, H = tuple(map(int, input().split()))
if W == 0 and H == 0:
    break
for i in range(1, W - 1):
    print("#" + "." * (H - 2) + "#")
print("#" * H)