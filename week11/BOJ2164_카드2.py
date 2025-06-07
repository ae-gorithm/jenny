# 백준 2164번. 카드2
# 1부터 N번까지 카드가 차례로 쌓여있음. 제일 위 한 장은 버리고, 그 다음 카드는 아래로 옮김. 마지막에 남는 카드 번호 구하는 문제.

from collections import deque

N = int(input())
queue = deque([i for i in range(1, N+1)])

answer = 0
while queue:
    answer = queue.popleft()
    if queue:
        answer = queue.popleft()
        queue.append(answer)

print(answer)
