x = int(input())
print('{}:{}:{}'.format(*[int(i) for i in (x//3600, x%3600//60, x%3600%60)]))