def main():
    a, b = map(int, input().split())
    print(" ".join([str(a // b), str(a % b), str(a / b)])