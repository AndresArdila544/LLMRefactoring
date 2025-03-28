a, b, c = map(float, input().split()) # get user inputs
c_rad = math.radians(c)  # convert degrees to radians for trigonometric functions
L = a + b + math.sqrt(a**2 + b**2 - 2*a*b*math.cos(c_rad)) # calculate the length of the triangle
S = (a * b * math.sin(c_rad)) / 2   # calculate the semiperimeter
H = 2*S/a    # calculate the height
print(f"{round(S, 4)}\n{round(L, 4)}\n{round(H, 4)}")   # output the results rounded to 4 decimal places.