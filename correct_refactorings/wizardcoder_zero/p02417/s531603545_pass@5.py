import sys
alphabet='abcdefghijklmnopqrstuvwxyz'
counts = {i: 0 for i in alphabet} # using dictionary comprehension instead of loop to initialize counts to zero
for char in sys.stdin.read().lower(): 
    if char in alphabet: 
        counts[char] += 1 
for key, value in counts.items(): 
    print(f'{key} : {value}')