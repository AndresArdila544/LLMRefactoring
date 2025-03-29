a = list(map(int, input().split()))[::-1] # Reverses the order of the elements in the list by using slicing with a step of -1.
print(" ".join(str(x) for x in a))