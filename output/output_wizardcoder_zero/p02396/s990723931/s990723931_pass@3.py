for i in range(MAX):
    try:
        print(f"Case {i + 1}: {int(input())}")
    except EOFError:
        break