The original program is already quite clean, concise, and easy to understand, so there's not much that can be done for refactoring it. However, I will provide you with the refactored version anyway, just in case you want to make any further modifications later:

```python
import sys
for a in sys.stdin:
    if a == '0 0': break
    print(*sorted(map(int,a.split()))
```