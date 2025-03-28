h, w = map(int, input().split())
while h and w:
    print("".join("#" * w + "\n" * (h - 3) + "#" + "." * (w-2) + "#\n" + "#" * w)
    h, w = map(int, input().split()) 
print()