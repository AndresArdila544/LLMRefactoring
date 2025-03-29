While 1:
    a, op, b = map(str, raw_input().split())
    a = int(a)
    b = int(b)
    print {
        "+": a+b,
        "-": a-b,
        "*": a*b,
        "/": a/b
    }.get(op)