def count_combinations(n, k):
    dp = [1] * (n + 1)

    for i in range(1, k):
        for j in range(2**i, n + 1):
            dp[j] += dp[j - 2**i]

    return dp[n] - 1

for _ in range(int(input())):
    n, k = map(int, input().split())
    print(count_combinations(n, k))