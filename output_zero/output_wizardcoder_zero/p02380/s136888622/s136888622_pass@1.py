a, b, C = map(int, input().split())
S = 0.5 * a * b * math.sin(C/180*math.pi)
L = a + b + math.sqrt((a**2 + b**2 - 2 * a * b * math.cos(C/180*math.pi))
h = b * math.sin(C/180*math.pi)
print(S, L, h, sep='\n')

# The refactored version of the code has fewer lines and improved readability by removing unnecessary variables.