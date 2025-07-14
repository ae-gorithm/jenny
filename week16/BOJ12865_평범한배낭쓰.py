# 백준 12865번. 평범한 배낭

# 배낭.. 무게와 가치.. DP 문제..!
# 물건의 개수 N, 무게 W, 가치 V, 최대 무게 K

"""
knapsack 문제: 가방의 무게 1~K 까지, 무게가 k일 때 담을 수 있는 가치의 최대를 구한다.
핵심 아이디어: wi 물건을 담는 경우, 가방의 가치는 vi + (가방의 무게가 w-wi일 때의 최대 가치)이다.

1. dp 배열: 2차원 배열
dp[물건][무게] vs. dp[무게][물건]
- dp[물건][무게] 방식으로 해야 한다.
- 하나의 물건에 대해 무게를 1~K까지 순차적으로 계산하므로, 무게 인덱스를 연속적으로 증가시키는 방법이 적절함.
- 배열은 메모리 상에 행 단위로 연속 저장되므로, 캐시 적중률 측면에서 유리함. 만약 dp[무게][물건] 방식으로 한다면 무게를 순차적으로 계산할 때 열 단위로 뛰어넘어야 함.

2. 물건은 무게 순으로 정렬한다. 적은 무게부터 탐색해야 하기 때문.
"""

N, K = map(int, input().split())
dp = [[0 for _ in range(K+1)] for _ in range(N + 1)]

arr = []
for _ in range(N):
    W, V = map(int, input().split())
    arr.append((W, V))
arr.sort()

for item in range(1, N+1):
    w, v = arr[item-1][0], arr[item-1][1] # 물건의 무게, 가치
    for k in range(1, K+1):
        if w > k: # 물건의 무게가 배낭 무게보다 큰 경우 (담을 수 없음)
            dp[item][k] = dp[item-1][k]
        else: # 같거나 작은 경우 (담을 수 있음)
            dp[item][k] = max(dp[item-1][k], v + dp[item-1][k-w]) # 담지 않는 경우, 담는 경우 비교

print(dp[N][K])
