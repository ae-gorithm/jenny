# 백준 2346번. 풍선 터뜨리기
from collections import deque

n = int(input())
queue = deque([_ + 1 for _ in range(n)])
moves = list(map(int, input().split()))
answer = []

for i in range(n - 1):
    cursor = queue.popleft()
    x = moves[cursor - 1]
    answer.append(cursor)

    # x만큼 이동
    # 양수면 왼쪽으로 이동
    # 음수면 오른쪽으로 이동
    if x > 0:
        for _ in range(x - 1):
            queue.append(queue.popleft())
    else:
        for _ in range(-1 * x):
            queue.appendleft(queue.pop())
    # print(i+1,"번 째: 터트린 풍선 ", cursor, ", 이동 수 ", x, ", 큐 ", queue)

answer.append(queue.popleft())
print(*answer)