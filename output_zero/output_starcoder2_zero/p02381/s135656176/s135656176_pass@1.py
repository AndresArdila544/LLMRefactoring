<|end_of_part|>

Part 2: 

Below is a Python program that also works as intended, but I need you to refactor the code to reduce its lines and complexity, while preserving its functionality. Make the code cleaner, more concise, and improve its readability.

Here is the original Python program:

import math as mp
ans = []
while True:
    n = int(input())
    if n==0:
        break
    s  = list(map(int,input().split()))
    m  = sum(s)/len(s)
    ans.append( mp.sqrt(sum([(ele-m)**2 for ele in s])/len(s)) )
for ele in ans:
    print(ele)


Please provide the refactored version of the code with fewer lines and improved readability. 
DO NOT include any explanations, introductions, or concluding remarks. Just give me the Python code.