Please provide the refactored version of the code with fewer lines and improved readability. DO NOT include any explanations, introductions, or concluding remarks. Just give me the Python code.

The following example shows how to refactor the above Python program:

while True:
    H,W = list(map(int, input().split()))
    if H == 0 and W == 0:
        break

    x = "#" * W
    for i in range(H):
        print(x)
    print()