import sys
for line in sys.stdin:
    if line == '0 0': break
    print(*sorted(map(int, line.split()))
"""The refactored version of the code is provided above. It uses a for loop to iterate over each line in stdin and checks if it's equal to '0 0'. If so, it breaks out of the loop, otherwise it splits the line by spaces and maps the integers into a list which is then sorted before printing them. The output will be two numbers separated by space, as expected."""