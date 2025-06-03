# 백준 2961번. 도영이가 만든 맛있는 음식
# 조합 라이브러리 쓰지 않고 재귀로 풀기
import sys

# idx를 증가시켜가며 포함했다/안했다 수행해보기

# 시간 복잡도: O(2^N * N)
# N개의 재료, 재료마다 선택/비선택 두 가지 경우의 수

def solve(i, s, b, cnt):
    global answer

    if cnt > 0:
        answer = min(answer, abs(s - b))
    if i == N:
        return

    solve(i + 1, s * arr[i][0], b + arr[i][1], cnt + 1) # i번째 재료를 포함하는 경우
    solve(i + 1, s, b, cnt) # i번째 재료를 포함하지 않는 경우


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = sys.maxsize

solve(-1, 1, 0, 0)
print(answer)
