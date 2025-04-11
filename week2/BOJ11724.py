# 백준 11724번. 연결 요소의 개수
# 문제: 방향 없는 그래프가 주어졌을 때, 연결 요수의 개수를 구한다.

from collections import deque

def bfs(graph, v, visit):
    queue = deque([v])
    while queue:
        x = queue.popleft()
        if visit[x]:
            continue
        visit[x] = True
        for nx in graph[x]:
            queue.append(nx)

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visit = [False] * (n + 1)

answer = 0
for i in range(1, n + 1):
    if not visit[i]:
        bfs(graph, i, visit)
        answer += 1

print(answer)
