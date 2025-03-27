print((lambda a, b, c: 'Yes' if a < b < c else 'No')(*map(int, input().split())))

This can be refactored to:

def yes_no(a, b, c):
    return "Yes" if a < b < c else "No"
print(yes_no(*map(int, input().split())))

This is more readable, concise and easier to understand. It also reduces the amount of lines in the code.