# 백준 9465번. 스티커
"""
뗄 수 있는 스티커의 점수의 최댓값

각 스티커: 최댓값.
1. 해당 스티커를 선택하는 경우
a c e
b d f
- e를 선택하는 경우: b, d를 봐야 함. (a를 보지 않아도 되는 이유: a가 포함되는 경우는 d에 포함되기 때문)
- f를 선택하는 경우: a, c를 봐야 함.

2. 해당 스티커를 선택하지 않는 경우는 고려하지 않음. 총 길이가 n이라고 했을 때, 길이 n에서 스티커를 선택하는 것이 무조건 이득이기 때문.


"""

T = int(input())
for _ in range(T):
    n = int(input())
    dp = [[0], [0]]
    dp[0].extend(list(map(int, input().split())))
    dp[1].extend(list(map(int, input().split())))

    for i in range(2, n+1):
        dp[0][i] += max(dp[1][i-1], dp[1][i-2])
        dp[1][i] += max(dp[0][i-1], dp[0][i-2])
    print(max(dp[0][n], dp[1][n]))
