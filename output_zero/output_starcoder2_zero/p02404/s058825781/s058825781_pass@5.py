"""


"""
Below is a Python program that works as intended, but I need you to refactor the code to reduce its lines and complexity, while preserving its functionality. Make the code cleaner, more concise, and improve its readability.

Here is the original Python program:

XS = list(map(int, open(0).read().split()))
for i in range(0, len(XS), 2):
    H = XS[i]
    W = XS[i+1]
    if H == 0 and W == 0:
        break
    print("#"*W)
    for _ in range(H-2):
        print("#{}#".format("." * (W-2)))
    print("#"*W)
    print("")


Please provide the refactored version of the code with fewer lines and improved readability. 
DO NOT include any explanations, introductions, or concluding remarks. Just give me the Python code.