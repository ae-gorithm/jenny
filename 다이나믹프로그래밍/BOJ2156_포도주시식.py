# 백준 2156번. 포도주시식
"""
연속 2개까지 가능.
현재 차례에서 선택하거나, 안 하거나 두 가지 경우가 있음.
현재 차례 i에서 선택하는 경우 ?xo 또는 xoo여야 함.
dp[i][0] = max(dp[i-1])
dp[i][1] = max(dp[i-1][0], dp[i-2][0]+arr[i-1]) + 자기 자신

입력: 6 10 13 9 8 1

0 0
0 6 # 초기값
6 16
16 23
"""

n = int(input())
glass = [int(input()) for _ in range(n)]

dp = [[0, 0] for _ in range(n+1)]
dp[1][1] = glass[0]

for i in range(2, n+1):
    dp[i][0] = max(dp[i-1])
    dp[i][1] = max(dp[i-1][0], dp[i-2][0] + glass[i-2]) + glass[i-1]

print(max(dp[n]))
