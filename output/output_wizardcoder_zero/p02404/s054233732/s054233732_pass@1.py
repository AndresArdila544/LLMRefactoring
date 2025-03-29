N = lambda: list(map(int, input().split())) # define N as a function that takes an input of two integers and returns them as a list of integers

while True:
    n1, n2 = N()  # use tuple unpacking to assign the values to variables
    if n1 + n2 == 0: # check if the sum of both values is 0 to break out of loop
        break
    
    for i in range(n1): # iterate over each row, starting with 0 and ending at n1 - 1
        print("#" * n2) # print "#" character n2 times for the first and last rows
        if i == 0 or i == n1 - 1:
            continue # skip printing characters for the first and last row
        
        s = '#' * (n2-2)
        print(f"#{s}#") # print "#" character with spaces in between
    
    print() # move to a new line at the end of each row