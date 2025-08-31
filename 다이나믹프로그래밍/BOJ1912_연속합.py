# 백준 1912번. 연속합
"""
연속된 몇 개의 수를 선택해 가장 큰 합을 구한다.

일차원 dp 배열.
dp[i] += max(dp[i-1], 0)
자기자신 차례에서는 무조건 자신이 포함되어야 함. 연속된 수열이기 때문.
1. 이전 연속된 수열을 이어가거나 -> dp[i-1] + dp[i]
2. 연속된 수열을 초기화하고 자신부터 시작하거나 -> dp[i]
"""

n = int(input())
dp = list(map(int, input().split()))

for i in range(1, n):
    dp[i] += max(dp[i-1], 0)
print(max(dp))
