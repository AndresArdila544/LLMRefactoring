while True:
     H,W = map(int,input().split())
     if H==0 and W==0: break
     idx = '#'*W + '\n'
     con = '#' + '.'*(W-2) + '#\n' * (H-2) if W > 2 else ''
     con += idx if H >= 2 else ''
     print(idx + con)