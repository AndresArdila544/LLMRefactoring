def print_substring(s, start, end):
    return s[start:(end + 1)]

def replace_substring(s, replacement, start, end):
    return s[:start] + replacement + s[(end + 1):]

def reverse_substring(s, start, end):
    substring = s[start:end+1]
    return s[:start] + substring[::-1] + s[end+1:]

S = input()
N = int(input())
for i in range(N):
    order = list(map(int, input().split()))
    if order[0] == "replace":
        S = replace_substring(S, order[3], order[1])
    elif order[0] == "reverse":
        S = reverse_substring(S, order[1], order[2])
    else:
        print_substring(S, order[1], order[2])