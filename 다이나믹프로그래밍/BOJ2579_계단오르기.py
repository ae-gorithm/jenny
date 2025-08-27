# 백준 2579번. 계단 오르기
"""
계단은 한 번에 한 계단/ 두 계단씩 오를 수 있다.
연속 세 개 계단을 밟으면 안 된다.*
계단을 밟아 얻을 수 있는 최대 점수 구하기.

2차원 배열을 둬야 한다. 바로 직전 계단에서 오는 경우(1)/ 두 전 계단에서 오는 경우(2)
(1) dp[n][0] = dp[n-1][1] + 자기 점수
(2) dp[n][1] = max(dp[n-2][0], dp[n-2][1]) + 자기 점수
"""

n = int(input())
score = [int(input()) for _ in range(n)]

dp = [[0, 0] for _ in range(n+1)]
dp[1] = [score[0], score[0]] # dp[0]은 시작점
for i in range(2, n+1):
    dp[i][0] = dp[i-1][1] + score[i-1]
    dp[i][1] = max(dp[i-2][0], dp[i-2][1]) + score[i-1]
print(max(dp[n][0], dp[n][1]))
