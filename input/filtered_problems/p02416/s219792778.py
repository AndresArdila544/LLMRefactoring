def calc_sum(n):
    total = 0
    while n> 0:
        #print(n//10, n% 10)
        total += n%10
        n//=10
    return total
    
while True:
    n = int(input())
    if n== 0:
        break
    print(calc_sum(n))
