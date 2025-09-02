# 백준 9251번. LCS
"""
LCS: 최장 공통 부분 수열.
두 수열이 주어졌을 때 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제.
ACAYKP & CAPCAK -> ACAK

(힌트 보고 풀었음)

두 문자열을 각각 행, 열으로 2차원 배열.
dp[i][j]: 문자열 A의 i번째, 문자열 B의 j번째까지의 LCS.
1. i번째, j번째 문자가 같은 경우: dp[i-1][j-1] + 1
  둘 다 직전 문자까지에서 한 문자씩 추가된 것이므로, A문자열 i-1번째, B문자열 j-1번째 + 1
2. 다른 경우: dp[i-1][j], dp[i][j-1] 중 최댓값.
  dp[i][j]가 되는 경우가 dp[i-1][j]에서 A문자열 하나 이동 or dp[i][j-1]에서 B문자열 하나 이동 이므로.
"""

A = list(input())
B = list(input())

dp = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)]

for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[len(A)][len(B)])
