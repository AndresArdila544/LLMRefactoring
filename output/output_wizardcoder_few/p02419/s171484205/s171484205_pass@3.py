n = int(input())
count_dict = {}
for _ in range(n):
    word = input().lower()
    count_dict[word] = count_dict.get(word, 0) + 1
print(max(count_dict.values()))
# Refactored version:
from collections import Counter
words = [input().lower() for _ in range(n)]
print(max(Counter(words).values())