# 백준 10844번. 쉬운 계단 수
"""
계단 수: 45656 처럼 인접한 모든 자리의 차가 1인 수.
길이가 N인 계단 수가 총 몇 개 있는지 구하기.

dp[i] = [x, x, x, x, x, x, x, x, x, x]
dp[i][j] = 길이가 i인 계단 수에서 마지막 자리가 j인 숫자의 개수

dp[i][0] = dp[i-1][1]
dp[i][1] = dp[i-1][0] + dp[i-1][2]
...
dp[i][8] = dp[i-1][7] + dp[i-1][9]
dp[i][9] = dp[i-1][8]
"""

N = int(input())
dp = [[0 for _ in range(10)] for _ in range(N)]
dp[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(1, N):
    for j in range(10):
        dp[i][j] = ((dp[i-1][j-1] if j>0 else 0) + (dp[i-1][j+1] if j<9 else 0)) % 1000000000
print(sum(dp[N-1])%1000000000)
