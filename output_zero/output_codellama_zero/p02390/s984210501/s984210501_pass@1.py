Here is the refactored code:

print(*(a//3600, a%3600//60, a%60), sep=':')