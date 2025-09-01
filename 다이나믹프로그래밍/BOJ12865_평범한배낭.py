# 백준 12865번. 평범한 배낭
"""
N개의 물건. 각 물건은 무게 W와 가치 V를 가진다.
무게 합이 K까지 가능할 때 최대 가치 합을 구한다.

1. i번째 물건을 담는 경우: (K-Wi)의 max값 + Vi
2. 안 담는 경우:

일차원 배열로도 가능할 것.

물건이 중복 사용되는 문제가 있음.
용량-아이템 순회 -> 아이템-용량(내림차순) 순회로 변경
dp[w-wi]가 이번 아이템을 반영하기 전 상태여야 하기 때문.
"""

N, K = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()

dp = [0] * (K+1)
for w, v in arr:
    for k in range(K, w-1, -1): # 물건을 한 번만 써야 하므로 내림차순.
        dp[k] = max(dp[k], # 물건을 안 담는 경우
                    dp[k-w] + v) # 물건을 담는 경우

print(max(dp))
