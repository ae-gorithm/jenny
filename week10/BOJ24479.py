# 백준 24479번. 알고리즘 수업 - 깊이 우선 탐색 1
# 노드의 방문 순서를 출력 (스택)

N, M, R = map(int, input().split())
arr = [[] for _ in range(N)]
for _ in range(M):
    i, j = map(int, input().split())
    arr[i-1].append(j-1)
    arr[j-1].append(i-1)
visited = [False] * N
answer = [0] * N

for a in arr:
    a.sort(reverse=True)

stack = []
order = 1
stack.append(R-1)

while stack:
    i = stack.pop()
    if not visited[i]:
        visited[i] = True
        answer[i] = order
        order += 1
    for j in arr[i]:
        if not visited[j]:
            stack.append(j)

for i in answer:
    print(i)
