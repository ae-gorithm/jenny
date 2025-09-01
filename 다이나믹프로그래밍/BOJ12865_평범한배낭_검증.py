# 백준 12865번. 평범한 배낭
"""
브루트포스로 구한 값과 DP로 구한 값을 비교해서 풀이를 검증하기 위함
"""

from itertools import combinations

def bf_bag(k, items):
    n = len(items)
    best = 0
    for r in range(n+1):
        for comb in combinations(range(n), r):
            w = sum(items[i][0] for i in comb)
            v = sum(items[i][1] for i in comb)
            if w <= k:
                best = max(best, v)
    return best

def dp_bag(k, items):
    dp = [0] * (k+1)
    for w, v in items:
        for i in range(k, w-1, -1): # 물건을 한 번만 써야 하므로 내림차순.
            dp[i] = max(dp[i], # 물건을 안 담는 경우
                        dp[i-w] + v) # 물건을 담는 경우
    return max(dp)+1

import random
for _ in range(10):
    N = random.randint(1, 10)
    K = random.randint(1, 50)
    items = [ (random.randint(1, 20), random.randint(0, 40)) for _ in range(N)]
    ans_dp = dp_bag(K, items)
    ans_bf = bf_bag(K, items)
    if ans_dp != ans_bf:
        print("실패 (", _+1, ")")
        print("입력: ")
        print(N, K)
        for item in items:
            print(item[0], item[1])
        print("정답: ", ans_bf, "오답: ", ans_dp)
        print("---------")
