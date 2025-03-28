def print_substring(string, a, b):
    print(string[a:b+1])

def replace_substring(string, new_str, a, b):
    return string[:a] + new_str + string[b+1:]

def reverse_substring(string, a, b):
    tmp = string[a:b+1]
    return string[:a] + tmp[::-1] + string[b+1:] 

S = input()
q = int(input())
for i in range(q):
    order = list(input().split())
    a = int(order[1])
    b = int(order[2])
    if order[0] == "replace":
        S = replace_substring(S, order[3], a, b)
    elif order[0] == "reverse":
        S = reverse_substring(S, a, b)
    else:
        print_substring(S, a, b)