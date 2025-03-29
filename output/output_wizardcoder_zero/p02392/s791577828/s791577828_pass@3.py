def comp_check():
    a, b, c = map(int, input().split())
    return 'Yes' if a < b and b < c else 'No'