Here is a cleaner and more concise version of your code:
s = int(input())
print(f"{s //3600}:{s % 3600 // 60}:{s % 3600 % 60}")