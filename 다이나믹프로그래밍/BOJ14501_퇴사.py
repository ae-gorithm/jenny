# 백준 14501번. 퇴사
"""
상담: 기간 T, 금액 P. 하루에 상담 1개만 가능.
상담을 골라서 얻을 수 있는 최대 수익 구하기.

뒤에서부터 앞으로. i일 상담을 선택하냐마냐
1. 선택하는 경우: dp[i] = dp[i+t] + p
2. 선택하지 않는 경우: dp[i] = dp[i+1]

"""

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]

dp = [0 for _ in range(N+1)]
for i in range(N-1, -1, -1):
    t, p = meetings[i]
    dp[i] = max(dp[i+t] + p if i+t <= N else 0,
                dp[i+1])
print(dp[0])
