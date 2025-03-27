import sys
EOL = 0
MAX = 10000
for i in range(MAX):
    x = int(input())
    if x == EOL:
        break
    print('Case {}: {}'.format(i + 1, x))