import re

def solve(input_string):
    q = int(input_string.split()[0])
    for _ in range(q):
        line = input_string.split()
        c = line[1]
        a = int(line[2]) + 1
        b = int(line[3]) + 1
        if c == "replace":
            result_string = re.sub(str[:a], str[a:b])
        elif c == "reverse":
            result_string = re.sub(str[:a], str[a:b][::-1])
        else:
            print(str[a:b])
    return result_string