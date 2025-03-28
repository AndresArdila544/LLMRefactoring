a = []
while True:
    value = int(input())
    if value == 0:
        break
    else:
        a.append(value)
for index, num in enumerate(a, start=1):
    print(f'Case {index}: {num}') 
# Refactored version with cleaner code without using unnecessary variables and while loop