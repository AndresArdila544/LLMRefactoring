a, b, c = map(int, input().split()) # Get user input for a, b, and c
if c <= 90:  # If c is less than or equal to 90
    print((b * math.sin(math.radians(c)) * a / 2) + (a+b) ) # Output the value of the first part of the calculation
    h = b * math.sin(math.radians(c)) # Calculate h using sin()
    A, B = sorted([a, b]) # Sort the values of a and b as variables A and B
    H = B * math.sin(math.radians(c)) # Calculate H using sin() and radians()
    X = (B**2 - H**2) ** 0.5 # Calculate X using the Pythagorean theorem
    C = ((A-X)**2 + H**2) ** 0.5 # Calculate C using Pythagorean theorem and additional calculation
    print(C+a+b) # Output the value of the second part of the calculation 
else: # If c is greater than 90
    print((b * math.sin(math.radians(c)) * a / 2) + (a-b) ) # Output the same as before, but with a different calculation for A and C
    A = abs(a-b*math.cos(math.radians(c)) # Calculate A using cos() and radians()
    h = b * math.sin(math.radians(c) # Calculate h as before
    x = (b**2 - h**2) ** 0.5 # Calculate the additional value for X
    c = ((A)**2 + h**2) ** 0.5 # Calculate C using Pythagorean theorem and abs() to handle negative values of A
    print(c+a+b) # Output the final result 
    print(h) # Output h as before

# Refactored version of code with fewer lines and improved readability.