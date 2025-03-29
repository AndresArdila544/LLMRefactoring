def main():
    s = list(input())
    n = int(input())
    
    for i in range(n):
        op = input().split()
        
        if op[0] == 'replace':
            rep = list(op[3])
            
            start, end = int(op[1]), int(op[2]) + 1
            for j in range(start, end):
                s[j] = rep[j - start]
                
        elif op[0] == 'reverse':
            sub_s = ''.join(s[start:end]).split()
            rev = list(sub_s[::-1])
            
            for j in range(start, end):
                s[j] = rev[j - start]
        else:
            print(''.join(s[start:end]))
        
main()