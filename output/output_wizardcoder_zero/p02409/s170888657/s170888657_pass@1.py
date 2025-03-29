data = [[0]*10 for _ in range(4)]
count = int(input())
for i in range(count):
    b, f, r, v = map(int, input().split())
    data[b-1][f-1] += v
    
for row in data:
    print(' '.join(map(str,row)) + '\n' if idx != len(data)-1 else ''.join(map(str,row)) + '#'*20 for idx,r in enumerate(data)