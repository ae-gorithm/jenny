# 백준 1021번. 회전하는 큐
# 문제: 주어진 숫자를 순서대로 뽑아낼 때 2, 3번 연산의 횟수 구하기.
# 디큐를 사용한다.
# (idx: 1~N)
# idx 1까지 왼쪽으로 이동하는 횟수가 더 적으면 왼쪽으로 이동 (2번 연산)
# idx N까지 오른쪽으로 이동하는 횟수 + 1이 더 적으면 오른쪽으로 이동 (3번 연산)

from collections import deque

N, M = map(int, input().split())
targets = list(map(int, input().split()))

deque = deque(range(1, N+1))
count = 0
for target in targets:
    idx = deque.index(target)
    if idx <= N - idx:
        deque.rotate(-idx)
        count += idx
    else:
        deque.rotate(N - idx)
        count += N - idx
    deque.popleft()
    N -= 1

print(count)