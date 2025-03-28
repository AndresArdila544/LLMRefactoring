S=input() + input() # concatenate strings to form a single string
if S.count(input()) == 0 and len(S) > 1: # if the count of the second input is zero and there are more than one character in the first input, then the result is 0 else it is 1.
    print('No')
else:
    print('Yes')