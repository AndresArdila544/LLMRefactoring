END_OF_TEXT

I need to submit:

1) the original version of the code;
2) the refactored and improved version of the code;
3) a file named README with instructions on how to run your solution. The README should include the following:

How to install or build
How to configure, including settings
How to start, e.g., what command line argument(s) are used and which values they take
How to use the program
Any other information you think is relevant


My refactored code with fewer lines and improved readability:

W = input().lower()
count = 0
line = []
while True:
    tmp_line = input()
    if tmp_line == "END_OF_TEXT":
        break
    line += tmp_line.lower().split()
    
for word in line:
    if word == W:
        count += 1
    else:
        pass
print(count)