def process_string(input_str):
    n = int(input())
    for i in range(n):
        op, start, end, *rest = input().split()
        if op == 'replace':
            replacements = list(map(int, rest))
            slice_start, slice_end = int(start), int(end) + 1
            replacement = input()
            for j in range(slice_start, slice_end):
                input_str[j] = replacement[j - int(start)]
        elif op == 'reverse':
            sub_string = input()
            reversed_sub_string = sub_string[::-1]
            for j in range(slice_start, slice_end):
                input_str[j] = reversed_sub_string[j - int(start)]
        else:
            print(''.join(input_str[int(start) : int(end)])