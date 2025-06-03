# 백준 2961번. 도영이가 만든 맛있는 음식
# 비트마스킹 풀이

# N개 재료의 선택/비선택을 비트로 표현 (조합 쓰지 않음)
# 1부터 2^N-1까지 모든 경우의 수 탐색

# 시간 복잡도: O(2^N * N)

import sys

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = sys.maxsize

for bit in range(1, 1 << N): # 예: 1001010101 -> 비트로 조합을 표현하는 것
    s, b = 1, 0
    for i in range(N):
        if bit & (1 << i):
            s *= arr[i][0]
            b += arr[i][1]
    answer = min(answer, abs(s - b))

print(answer)

# 1. 비트마스킹
# - 구현이 가장 직관적이고 빠름
# - 내부적으로 부분집합 선택이 메모리적으로도 효율적(비트연산)
# - 파이썬에서 for문/비트연산이 재귀 호출보다 더 빠른 경향
#  → 실행 속도, 메모리 사용 모두 제일 우수
#
# 2. 재귀(백트래킹)
# - 함수 호출 스택이 쌓여서 오버헤드가 발생
# - (단, N이 작으니 현실적으론 무시할 수준)
# - 파이썬 재귀는 매우 깊어지면 recursion limit 이슈가 있을 수 있음(여기선 해당 X)
# - 구현은 직관적이지만, 비트마스킹보다 느릴 수 있음
#
# 3. combinations
# - itertools는 내부적으로 빠르게 동작하지만,
# - 조합 객체를 메모리로 만들고 iterate해야 하니,
# - 재귀/비트마스킹보다는 미세하게 느릴 수 있음(역시 N이 작으니 의미 없음)