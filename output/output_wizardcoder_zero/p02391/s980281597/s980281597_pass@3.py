def compare_numbers(a, b):
    return "a > b" if a > b else ("a < b" if a < b else "a == b")

s = input().split()
print(compare_numbers(*map(int, s))