def main():
    while True:
        n = int(input())
        if n == 0:
            break
        
        else:
            b_list = list(map(int, input().split()))
            ave = sum(b_list) / n
            A = [(ave - x) ** 2 for x in b_list]
            p = math.sqrt(sum(A) / n)
            print("{:.8f}".format(p))
            A.clear()
    
if __name__ == "__main__":
    main()