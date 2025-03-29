def process_string(s):
    for _ in range(int(input())):
        op, a, b = input().split()
        if op == "replace":
            s = s[:int(a)] + input() + s[int(b) + 1:]
        elif op == "reverse":
            s = s[:int(a)] + s[int(a):int(b)][::-1] + s[int(b):]
        else:
            print(s[int(a):int(b)])

str = input()
process_string(str)