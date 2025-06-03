# 백준 2961번. 도영이가 만든 맛있는 음식
# 신맛 S: 곱, 쓴맛 B: 합
# 재료 N개를 선택해 S의 곱과 B의 합의 차이를 작게 만든다. (N: 1~10)

# N개 중 1개, 2개, 3개, ..., 10개
# 조합 써서 브루트포스 ?

# 시간 복잡도: O(N * 2^N)
# 총 조합 수: 2^N
# 각 조합 당: O(N)

from itertools import combinations
import sys

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = sys.maxsize
for i in range(1, N + 1):
    for comb in combinations(arr, i):
        s = 1
        b = 0
        for food in comb:
            s *= food[0]
            b += food[1]

        answer = min(answer, abs(s - b))

print(answer)
