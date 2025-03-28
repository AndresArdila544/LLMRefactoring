Here's the refactored version:
 
 Taro = Hanako = 0
 n = int(input())
 for i in range(n):
     T, H = input().split()
     if int(T) > int(H):
         Taro += 3
     elif int(T) == int(H):
         Taro += 1
         Hanako += 1
     else:
         Hanako += 3
 print(Taro, Hanako)