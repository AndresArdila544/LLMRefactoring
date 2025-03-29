def multiply_and_double(l):
    a, b = map(int, l.split())
    print(a * b, 2*(a + b))

if __name__ == "__main__":
    multiply_and_double(input())