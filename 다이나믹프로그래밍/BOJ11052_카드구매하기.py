# 백준 11052번. 카드 구매하기
"""
카드팩 N가지: 인덱스 번호가 카드 개수이고, 값이 비용임.
정확히 카드 N개를 사기 위해 최대 비용을 지불하도록 카드팩을 고른다. -> 이때 최대 비용 구하기.
(카드팩 개수는 무한인듯)

일차원 배열
dp[n]: n개를 살 때 최대 비용
마지막으로 고른 카드팩만 고려.
dp[n] = max(dp[n], dp[n-1] + dp[1], dp[n-2] + dp[2], ... , 2*dp[n/2])
dp[n-1] = max(dp[n-1], dp[n-2] + dp[1], ..., 2*dp[(n-1)/2])
시간복잡도 O(N^2)
"""
import math

N = int(input())
dp = list(map(int, input().split()))

for i in range(1, N):
    for j in range(1, math.ceil(i/2)+1):
        dp[i] = max(dp[i], dp[i-j] + dp[j-1])
print(dp[N-1])
