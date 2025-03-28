refactored_code = """
W = input()
count = 0
for line in iter(lambda: input(), "END_OF_TEXT"):
    count += sum(1 for word in line.lower().split() if word == W)
print(count
"""
# This code is more concise and reduces the number of lines used as compared to the original version. The lambda function replaces the while loop and allows us to use a generator expression with the iter() built-in function to read input until the "END_OF_TEXT" string is encountered.