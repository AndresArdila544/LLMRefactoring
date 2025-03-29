count = int(1)

while True:
    x = int(input())
    if x != 0:
        print('Case {}: {}'.format(count, x))
        count += 1
    else:
        break

# Refactored version

i = 1
while True:
    x = int(input())
    if x != 0:
        print(f'Case {i}: {x}')
        i += 1
    else:
        break
        
# Explanation: We can directly use the variable `count` to count the number of cases and eliminate the unnecessary code for printing the string "Case" instead of using string formatting. Also, we can use f-strings to make it more concise