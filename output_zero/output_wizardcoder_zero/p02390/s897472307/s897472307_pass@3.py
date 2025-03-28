a = input()
h, m, s = a // 360, (a % 360) // 60, a % 60 # Using tuple unpacking to assign variables h, m and s directly from integer division and modulus.
print("{}:{}:{}".format(h, m, s))