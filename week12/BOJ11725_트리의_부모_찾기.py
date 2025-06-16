# 백준 11725번. 트리의 부모 찾기
# 루트 없는 트리가 주어진다. 트리의 루트를 1이라고 정했을 때 각 노드의 부모를 구하는 프로그램을 작성.

# 1부터 시작해서 탐색을 해야 함. BFS/DFS 뭘로 해도 상관 없을 거 같음.
# 부모를 적을 배열 하나 필요.
# BFS 말고 입력만을 순회하면서 하는 법?

from collections import deque

N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

visited = [False] * N
answer = [0] * N
queue = deque([0])

while queue:
    s = queue.popleft()
    visited[s] = True
    for i in graph[s]:
        if not visited[i]:
            answer[i] = s
            queue.append(i)

for i in range(1, N):
    print(answer[i] + 1)
