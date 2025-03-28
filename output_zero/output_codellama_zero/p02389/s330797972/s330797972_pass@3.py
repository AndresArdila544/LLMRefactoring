Here is the refactored version of the original Python program:
num = input()
l = num.split(" ")
a, b = (int(i) for i in l)
print(a*b, end="")
print(" ", end="")
print(a*2+b*2)