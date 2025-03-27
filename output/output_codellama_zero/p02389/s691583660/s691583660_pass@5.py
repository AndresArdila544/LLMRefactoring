Here is a possible refactored version of the code:

def main():
    l = input()
    print(*map(lambda x:x*2, map(int, l.split())), sep='\n')

if __name__ == "__main__":
    main()