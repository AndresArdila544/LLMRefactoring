n = int(input())
 cards = [input().split() for i in range(n)]
 p_taro =0
 p_hanako=0
 for i in range(n):
   if cards[i][1]>cards[i][0]:# Hanako wins 3 points
     p_hanako+=3
   elif cards[i][0]<cards[i][1]: #Taro wins 3 points
     p_taro+=3
   else: # Tie, both win 1 point
     p_taro+=1
     p_hanako+=1
 print(p_taro, p_hanako)