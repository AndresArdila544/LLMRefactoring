def process_string(S):
    q = int(input())
    for _ in range(q):
        order = list(map(int, input().split()))
        if order[0] == "replace":
            S = S[:order[1]] + order[3] + S[order[4]:]
        elif order[0] == "reverse":
            tmp = S[order[1]:order[2]+1][::-1]
            S = S[:order[1]] + tmp + S[order[2]+1:] 
        else:
            print(S[order[1]:order[2]+1])
            
S = input()
process_string(S)