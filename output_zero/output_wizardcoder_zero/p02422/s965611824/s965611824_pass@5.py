def process_operations(s: str, q: int):
    for _ in range(q):
        o = input().split()
        if o[0] == 'replace':
            s = s[:int(o[1])] + o[3] + s[int(o[2])+1:]
        elif o[0] == 'reverse':
            rev = s[int(o[1]): int(o[2]+1)]
            s = s[:int(o[1])] + rev[::-1] + s[int(o[2]+1:]
        elif o[0] == 'print':
            print(s[int(o[1]): int(o[2]+1)

# This program takes a string `s` as input, then processes `q` number of operations. Each operation is one of the following: 
# - replace: replace a substring starting at index `i` with another substring specified by `o[3]` (inclusive), ending at index `j` (exclusive)
# - reverse: reverse a substring starting at index `i` and ending at index `j` (inclusive)
# - print: print the substring starting at index `i` and ending at index `j` (exclusive) 

# The original code reads each line of input, splits it into tokens using spaces as delimiters, and performs the corresponding operation on `s`. Then, it either replaces a substring or reverses another substring. 
# Finally, it prints the resulting substring if the operation is print.