XS = list(map(int, open(0).read().split()))
for H, W in zip(*[iter(XS)]*2):
    if H == 0 and W == 0:
        break
    print("#" * (W + 2) + "".join(". " * ((H - 2) // 2)) + "#" * (W + 2))
"""The zip(*[iter(XS)]*2) will create an iterator that yields pairs of consecutive elements from the list XS, effectively dividing it into tuples of height and width. Then, we can iterate over those pairs using a for loop and use the if statement to check if both are non-zero, and print them accordingly."""