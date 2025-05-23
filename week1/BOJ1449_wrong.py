# 백준 1449번. 수리공 항승
# 문제: 물이 새는 곳 N개에 길이 L의 테이프를 붙일 때, 필요한 테이프의 최소 개수를 구한다.

# 고려사항 1. N이 같더라도 위치에 따라 최소 개수가 달라진다. (테이프는 잘라서 사용할 수 없기 때문)
# ex) 테이프 길이가 3일 때
#     0 1 1 0 0 1 -> 2개 필요
#     0 1 1 1 0 0 -> 1개 필요
# 고려사항 2. 연속되지 않더라도 테이프 길이 이내면 테이프 1개로 가능하다.
# ex) 테이프 길이가 4일 때
#     0 1 1 1 1 0 ... -> 1개 필요
#     0 1 0 0 1 0 ... -> 1개 필요
#     0 1 0 0 0 1 ... -> 2개 필요

# 방법
# 1. 정렬
# 2. 테이프 1개로 붙일 수 있는 구간을 구한다.
# 3. 각 부분마다 ceil(num/L)값을 더하고, 모든 값을 합한다. (시그마 ceil(num/L))

# 반례
# 6 3
# 1 2 3 5 6 7
# 출력: 3
# 답: 2

import math

N, L = map(int, input().split())
spot = list(map(int, input().split()))

spot.sort()

answer = 0
num = 1

for i in range(N):
    if i == N - 1:
        answer += math.ceil(num / L)
        break
    if spot[i + 1] <= spot[i] + L - 1:
        num += spot[i + 1] - spot[i]
    else:
        answer += math.ceil(num / L)
        num = 1

print(answer)