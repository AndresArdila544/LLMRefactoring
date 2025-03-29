def count_word(w):
    counter = 0
    for i in stdin.read().lower().split():
        if i == w:
            counter += 1
    print(counter)

Refactored version:

import sys
count = sum(map(lambda word: word.lower() == w, sys.stdin.read().strip().split()))
print(count)