# 백준 11727번. 2xn 타일링 2
"""
2xn 타일링 문제에 2x2 크기의 타일이 추가됨.

dp[n] = dp[n-1] + dp[n-2]*2
"""
n = int(input())
dp = [1] * (n+1)
for i in range(2, n+1):
    dp[i] = (dp[i-1] + 2 * dp[i-2]) % 10007
print(dp[n])
