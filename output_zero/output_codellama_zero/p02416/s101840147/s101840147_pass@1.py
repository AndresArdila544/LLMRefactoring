while True:
    try:
        input = raw_input()
        if input == '0': break
        print sum(map(int, input))
except ValueError:
    break