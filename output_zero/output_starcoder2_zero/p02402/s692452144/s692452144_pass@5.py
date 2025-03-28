"""
# My solution:
def minmax(list1):
    return (min(list1), max(list1))

def sum1(list1):
    return sum(list1)

print "Please input the numbers:"
n = int(raw_input()) # Get a number from user to use as the length of list1.
list1 = [] # Make an empty list, and append elements to it.
for i in range(0, n):
    list1 += [int(raw_input())]
print minmax(list1), sum1(list1)