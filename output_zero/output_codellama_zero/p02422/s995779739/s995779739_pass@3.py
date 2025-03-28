def print_slice(sequence, start, end):
    return sequence[start:end+1]

def replace(sequence, replace_with, start, end):
    return sequence[:start] + replace_with + sequence[end+1:]

def reverse(sequence, start, end):
    return sequence[:start] + sequence[start:end+1][::-1] + sequence[end+1:]

S = input()
q = int(input())

for _ in range(q):
    command, a, b, *rest = input().split()
    if command == "print":
        print_slice(S, int(a), int(b))
    elif command == "replace":
        S = replace(S, "".join(rest), int(a), int(b))
    elif command == "reverse":
        S = reverse(S, int(a), int(b))