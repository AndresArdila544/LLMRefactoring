def main():
    while True:
        n, x = map(int, input().split())
        if n+x == 0:
            break
        ans = 0
        for i in range(1, n):
            for j in range(i+1, n):
                if j < x-i-j <= n:
                    ans += 1
        print(ans)

# Explanation:
# The original program takes two integers as input from the user and calculates the number of pairs of distinct numbers (i, j) where i < j such that i + j = x - i - j. 
# It does this by iterating through all possible values of i and j in the range [1, n-1], and checking if they satisfy the given condition. The loop is nested to handle both the cases where i > j and i < j.
# The program runs until it encounters a line with two zeros, indicating that there are no more inputs left to process.