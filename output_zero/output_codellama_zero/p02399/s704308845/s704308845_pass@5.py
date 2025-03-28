Here is the refactored version of the code:

#!/usr/bin/python

a, b = map(int, input().split())
print(str(a//b) + " " + str(a%b) + " " + str(a//b))