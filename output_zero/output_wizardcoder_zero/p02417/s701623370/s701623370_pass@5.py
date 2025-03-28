s=input().lower()
print('\n'.join(f"{chr(i)} : {s.count(chr(i))}" for i in range(97, 123)))