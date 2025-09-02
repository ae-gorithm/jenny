# 백준 11660번. 구간 합 구하기 5
"""
dp[i][j]: (1,1)부터 (i,j)까지 합
(x1, y1)부터 (x2, y2)까지 합: dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] - dp[x1-1][y1-1]
"""
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for i in range(N+1)] for j in range(N+1)]

# 누적합 구하기
for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j] = arr[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])
