# 백준 2293번. 동전 1
"""
n가지 동전을 사용해서 합이 k가 되도록 하는 경우의 수. 동전의 개수는 무한.

i번째 동전의 가치 vi.
dp[k] = dp[k-v1] + dp[k-v2] + ... + dp[k-vn]

이차원 배열. 가로는 동전, 세로는 가치
이차원 배열로 하는 경우 메모리 초과 (최대 100*10000 크기의 배열이 만들어짐)
-> 일차원 배열로 변경
기존에는 탐색을 아이템순으로 했는데, 가치순으로 해야함.
"""
n, k = map(int, input().split())
val = [int(input()) for _ in range(n)]
val.sort()

# 3. 일차원 배열 풀이 (동전 -> 가치)
dp = [0 for _ in range(k+1)]
dp[0] = 1
for v in val: # 동전
    for i in range(v, k+1):
        dp[i] += dp[i-v]
print(dp[k])

# 2. 일차원 배열 풀이 (가치 -> 동전)
# 아래 처럼 푸는 경우, 12와 21이 다르게 처리되어 중복이 생김
# dp = [0 for _ in range(k+1)]
# dp[0] = 1
# for i in range(k+1):
#     for v in val:
#         if i-v < 0:
#             break
#         dp[i] += dp[i-v]
# print(dp[k])

# 1. 이차원 배열 풀이 (동전 -> 가치)
# dp = [[0 for _ in range(n)] for _ in range(k+1)]
#
# for i in range(n):
#     v = val[i]
#     dp[v][i] = 1
#     for j in range(v+1, k+1):
#         for c in range(0, i+1):
#             dp[j][i] += dp[j-v][c]
# answer = 0
# for i in range(n):
#     answer += dp[k][i]
# print(answer)
