while True:
    try:
        x = int(input())
        if x == 0:
            break
        print(f"Case {i + 1}: {x}")
    except ValueError:
        continue