```python
while True:
    H, W = map(int, input().split()) # Take input for height and width of pattern
    if not (H or W): # If both H and W are 0, break out of the loop
        break
    
    pattern_string = "."*(W//2) + "#" + "."*(W%2) # Create a pattern string with alternating hashes and dots
    
    for i in range(H): # Loop through each row of the pattern
        if i & 1: # If the row number is odd, print the pattern in reverse order
            print(pattern_string[::-1]) # Print the reversed string
        else: # If the row number is even, print the pattern as is
            print(pattern_string)
```