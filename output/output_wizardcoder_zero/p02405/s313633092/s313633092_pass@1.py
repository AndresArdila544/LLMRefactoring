a, b = map(int, input().split())
while a != 0 and b != 0:
    b_even, b_odd = ".", "#" * b
    
    for i in range(a):
        print((b_odd if i%2 else b_even) * b + "\n")