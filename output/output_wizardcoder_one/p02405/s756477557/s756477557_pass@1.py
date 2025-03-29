import sys
print('\n'.join(''.join('#.' * (2*i + 1) for i in range(30)) if not i % 2 else ' '*(30 - i) for i in range(15)))