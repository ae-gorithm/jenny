# 백준 11053번. 가장 긴 증가하는 부분 수열
"""
각 위치까지 왔을 때의 최대 길이를 저장하기
감소하는 부분에서는 이전 최대 길이를 가져오기
이전 최대 길이일 때 마지막 숫자도 함께 저장해야 하니까 2차원 배열이 필요 (?) -> (x)

dp[n] = [최대 길이, 마지막 숫자]
if dp[n][1] > dp[n-1][1]:
    dp[n] = [dp[n-1][0]+1, dp[n]]
else:
    dp[n] = dp[n-1]

위 반례
1 2 10 5 6
오답: 3 (1, 2, 10)
정답: 4 (1, 2, 5, 6)

배낭 문제처럼 1000x1000 배열을 만들어야 하나 ..
"""

n = int(input())
seq = list(map(int, input().split()))

dp = [0 for _ in range(n)]
for i in range(n):
    for j in range(0, i):
        if seq[j] < seq[i]:
            dp[i] = max(dp[j] + 1, dp[i])
print(max(dp)+1)
