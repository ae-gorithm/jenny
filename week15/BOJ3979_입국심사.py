# 백준 3079번. 입국심사

# 사람 M명, 문 N개(k번 문의 심사 시간: Tk)
# 최대한 빨리 모두가 심사 받기
# 비어도 안 가고 기다릴 수 있음.

"""
<파라메트릭 서치>
최적화 문제를 결정 문제로 바꾸고 이분 탐색을 한다.
정답이 될 수 있는 값들이 연속적이어야 한다.

문제를 파라미트릭 서치로 풀어보기
모든 사람이 언젠간 심사를 다 받을 수 있음.
-> 모든 시간을 탐색(이분탐색)하면서 그 시간 내에 가능한지 확인

가능한지 확인하는 함수 짜야함:
각 심사대에서 그 시간 동안 몇 명 가능한지 계산. 값들 합해서 최솟값 업데이트.
"""

N, M = map(int, input().split())
gates = []
for _ in range(N):
    gates.append(int(input()))

def isCompleted(t):
    sum = 0
    for i in range(N):
       sum += t // gates[i]
    if sum >= M:
        return True

left = 0
right = min(gates) * M
answer = right
while left <= right:
    mid = (right + left) // 2
    if mid == left or mid == right:
        break
    if isCompleted(mid):
        answer = min(answer, mid)
        right = mid
    else:
        left = mid

    # 입국 심사 가능한 최소 값 구하기 -> 왼쪽으로 계속 줄여가야 함.
    # isCompleted가 True이면 왼쪽으로 더 줄여보기
    # isCompleted가 False이면 오른쪽으로 더 늘리기
    # 멈추는 때:

print(answer)
