refactored_code = """
n=int(input())
a=[i for i in range(1, n+1) if i%3==0 or (i//10)%3==0]
print(*a)"""