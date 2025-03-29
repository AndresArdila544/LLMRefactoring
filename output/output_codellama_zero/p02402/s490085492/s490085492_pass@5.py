Here is a more concise and well-written program:

n = sys.stdin.readlines()[1].split(" ")
print(f"{min(n)} {max(n)} {sum(map(int, n))}")