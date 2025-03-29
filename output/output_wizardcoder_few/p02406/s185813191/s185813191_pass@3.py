n = int(input())
for i in range(1, n+1):
    if (i % 3 == 0) or ('3' in str(i)):
        print('', i, end='')
print()

The refactored version of the code reduces the number of lines and improves its readability as it eliminates unnecessary operations. It also uses a shorter if statement with the same functionality by checking whether i is divisible by 3 or contains '3' as a substring using the `or` operator. The original code was already optimized in terms of functionality, but the refactored version reduces its complexity and length while still achieving the same output.