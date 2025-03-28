#Solution:
def taro(n):
    score = {'Taro':0,'Hanako':0}

    for i in range(n):
        T,H = map(str, input().split())

        if T > H:
            score['Taro'] += 3
        
        elif T == H:
            score['Taro'] += 1
            score['Hanako'] += 1

        else:
            score['Hanako'] += 3
    
    return score