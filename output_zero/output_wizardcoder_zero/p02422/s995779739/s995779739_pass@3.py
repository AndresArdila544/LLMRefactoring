def process_order(S):
    q = int(input())
    
    for i in range(q):
        order = list(map(int, input().split()))
        if order[0] == "replace":
            S = S[:order[1]] + order[3] + S[order[4]:]
        elif order[0] == "reverse":
            tmp = S[order[1]:order[2]+1]
            S = S[:order[1]] + tmp[::-1] + S[order[2]+1:]
        else:
            print(S[order[1]:order[2]+1])
            
def main():
    S = input()
    process_order(S)