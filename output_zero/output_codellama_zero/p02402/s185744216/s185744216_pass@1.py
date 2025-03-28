from typing import List
a: str = input()
table: List[int] = list(map(int, input().split()))
print(*sorted(table), sum(table))