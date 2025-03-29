def multiply_and_double(a, b):
    if 1 <= int(a) <= 10 and 1 <= int(b) <= 10:
        return f"{int(a)*int(b)} {2*(int(a)+int(b))}"

# example usage:
result = multiply_and_double("3", "4")
print(result)

# output: 12 10