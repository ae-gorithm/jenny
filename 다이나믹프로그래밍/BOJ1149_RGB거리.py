# 백준 1149번. RGB거리
"""
1. 1번 != 2번
2. N-1번 != N번
3. i번 != i-1번, i번 != i+1번
=> 직전 집이랑만 색깔이 다르면 됨.
집 칠하는 최소 비용 구하기.
각 집마다 비용 다름.
이전 집까지의 최소 비용 + 현재 최소 비용

2차원 배열. dp[n]: 길이 3 배열 (빨/초/파 색깔별 최소 비용)
"""

n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(3): # 현재 집 색깔을 빨/초/파를 고르는 경우
        costs[i][j] += min(costs[i-1][(j+1)%3], costs[i-1][(j+2)%3])
print(min(costs[n-1]))
