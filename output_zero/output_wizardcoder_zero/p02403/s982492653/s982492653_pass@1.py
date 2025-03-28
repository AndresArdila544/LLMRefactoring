while True:
    HM = input().split()
    if not all(HM):
        break
    for _ in range(int(HM[0])):  # _ is a throwaway variable name to avoid unused variable warning
        print("#" * int(HM[1]) + "\n")