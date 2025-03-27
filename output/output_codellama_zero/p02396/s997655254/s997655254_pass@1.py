i = 0
while True:
    try:
        x = int(input())
    except ValueError:
        break
    i += 1
    print(f"Case {i}: {x}")