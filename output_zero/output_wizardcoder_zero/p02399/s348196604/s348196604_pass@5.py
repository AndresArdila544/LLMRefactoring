a, b = map(int, input().split()) # using input() instead of raw_input() for python3 compatibility and better readability
d, r, f = a // b, a % b, round(float(a)/float(b), 7) # separate assignment to improve clarity and reduce lines
print(*[d,r,f]) # unpacking the variables in print statement using *