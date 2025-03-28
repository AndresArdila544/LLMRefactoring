Below is a Python program that works as intended, but I need you to refactor the code to reduce its lines and complexity, while preserving its functionality. Make the code cleaner, more concise, and improve its readability.

Here is the original Python program:

T=0
H=0
n=int(input())
for i in range(n):
    s=input()
    s=s.rstrip().split()
    if s[0]==s[1]:
        T+=1
        H+=1
    else:
        t=[s[0],"t"]
        h=[s[1],"h"]
        S=[t,h]
        S.sort()
        if S[1][1]=="t":
            T+=3
        elif S[1][1]=="h":
            H+=3
print(T,H)


Please provide the refactored version of the code with fewer lines and improved readability. 
DO NOT include any explanations, introductions, or concluding remarks. Just give me the Python code.