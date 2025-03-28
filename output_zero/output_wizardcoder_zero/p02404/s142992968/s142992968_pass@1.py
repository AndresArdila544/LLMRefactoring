def print_pattern(h, w):
    if h == 0 and w == 0: return ""
    idx = "#" * w + "\n"
    con = ""
    if w > 2:
        for _ in range(1, h-2):
            con += "#."*(w-2) + "#\n"
    if h >= 2:
        return idx + con
    else:
        return idx + (idx * (h-2))

print_pattern(*map(int, input().split()))

#The refactored code is much more concise and easier to read. It uses a for loop instead of recursion for printing the pattern, which makes it faster and more efficient. The function takes two arguments h and w, which are integers representing the height and width respectively, and returns the pattern as a string.