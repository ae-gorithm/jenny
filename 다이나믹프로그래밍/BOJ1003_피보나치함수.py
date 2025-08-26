# 백준 1003번. 피보나치 함수
"""
피보나치 함수를 재귀로 구현했을 때, 0과 1이 각각 몇 번 출력되는지

dp[n] = dp[n-1] + dp[n-2]
n일 때 출력 횟수 = n-1일 때 출력 횟수 + n-2일 때 출력 횟수

1,0 구분해야 함 -> 배열 따로 두기 / 2차원 배열로 두기

초기값:
dp[0] = [1, 0]
dp[1] = [0, 1]
"""

T = int(input())
testcase = [int(input()) for _ in range(T)]
n = max(testcase)

dp = [[0, 0] for _ in range(n+1)]
dp[0] = [1, 0]
if n >= 1:
    dp[1] = [0, 1]
    for i in range(2, n + 1):
        dp[i][0] = dp[i-1][0] + dp[i-2][0]
        dp[i][1] = dp[i-1][1] + dp[i-2][1]

for t in testcase:
    print(dp[t][0], dp[t][1])
