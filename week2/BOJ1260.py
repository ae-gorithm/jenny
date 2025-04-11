# 백준 1260번. DFS와 BFS
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력한다. 방문 가능한 정점이 여러 개인 경우, 정점 번호가 작은 것을 먼저 방문한다. 더 이상 방문할 수 없는 경우 종료한다.

from collections import deque

def dfs(graph, x, visit, result):
    result.append(x)
    visit[x] = True
    for nx in graph[x]:
        if not visit[nx]:
            dfs(graph, nx, visit, result)

def bfs(graph, visit):
    queue = deque([v])
    result = []
    while queue:
        x = queue.popleft()
        if visit[x]:
            continue
        result.append(x)
        visit[x] = True
        for nx in graph[x]:
            queue.append(nx)
    return result

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    v1, v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for edges in graph:
    edges.sort()

result_dfs = []
visit_dfs = [False] * (n + 1)
dfs(graph, v, visit_dfs, result_dfs)
print(*result_dfs)

visit_bfs = [False] * (n + 1)
result_bfs = bfs(graph, visit_bfs)
print(*result_bfs)
