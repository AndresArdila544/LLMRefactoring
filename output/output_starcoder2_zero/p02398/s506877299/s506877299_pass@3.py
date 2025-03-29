The original text is: 

Below is a Python program that works as intended, but I need you to refactor the code to reduce its lines and complexity, while preserving its functionality. Make the code cleaner, more concise, and improve its readability.

Here is the original Python program:

a,b,c = map(int,raw_input().split())
lst = []
for i in range(a,b+1):
	if c%i == 0:
		lst.append(i)
print len(lst)

Please provide the refactored version of the code with fewer lines and improved readability. 
DO NOT include any explanations, introductions, or concluding remarks. Just give me the Python code.