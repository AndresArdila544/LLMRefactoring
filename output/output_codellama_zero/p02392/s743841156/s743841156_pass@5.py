def lessthen (a, b):
    return a < b
    
def range (a, b, c):
    return lessthen(a, b) and lessthen(b, c)

def main():
    a, b, c = map(int, input().split())
    if range(a, b, c):
        print('Yes')
    else:
        print('No')
    
if __name__ == "__main__":
    main()