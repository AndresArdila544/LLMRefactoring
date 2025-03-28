Here is the refactored version of the code:

w = input()
c = sum(s.lower().split().count(w) for s in iter(input, "END_OF_TEXT"))
print(c)