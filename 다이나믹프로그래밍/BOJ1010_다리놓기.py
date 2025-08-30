# 백준 1010번. 다리 놓기
"""
왼쪽 N개, 오른쪽 M개. 겹치지 않게 점을 잇는 경우의 수.
오른쪽 M개 중 N개를 고르면 됨. mCn (조합)

-> DP로 푸는 법?

"""
dp = [[0] * 31 for _ in range(31)] # dp[i][j] = i개 중 j개를 고르는 경우의 수

for i in range(31):
    dp[i][0] = 1     # iC0 = 1
    dp[i][i] = 1     # iCi = 1

for i in range(1, 31):
    for j in range(1, i):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    print(dp[m][n])
