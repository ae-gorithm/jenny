# 백준 1932번. 정수 삼각형
"""
dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + dp[i][j] (단, j-1>=0, j<n)
"""

n = int(input())
dp = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(i+1):
        # if j == 0:
        #     dp[i][j] += dp[i-1][j]
        # elif j == i:
        #     dp[i][j] += dp[i-1][j-1]
        # else:
        #     dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])
        dp[i][j] += max(
            dp[i - 1][j - 1] if j > 0 else 0,
            dp[i - 1][j] if j < i else 0
        )
print(max(dp[n-1]))
