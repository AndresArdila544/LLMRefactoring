def main():
    while True:
        x = int(input())
        if x == 0:
            break
        
        digit_sum = sum(int(digit) for digit in str(x))
        print(digit_sum)

main()