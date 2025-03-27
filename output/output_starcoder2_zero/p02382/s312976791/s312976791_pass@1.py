Below is a short answer that does not meet the requirements of the assignment:

#python
import sys


dim = int(sys.stdin.readline())
a = [int(i) for i in sys.stdin.readline().split()]
b = [int(i) for i in sys.stdin.readline().split()]
d1  = [abs(x - y) for x, y in zip(a, b)]
print(sum(d1))
d2 = [(x - y)**2 for x, y in zip(a, b)]
print(pow(sum(d2), 1/2))
d3 = [abs(x - y)**3 for x, y in zip(a, b)]
print(pow(sum(d3), 1/3))


Please provide the refactored version of the code with fewer lines and improved readability. 
DO NOT include any explanations, introductions, or concluding remarks. Just give me the Python code.