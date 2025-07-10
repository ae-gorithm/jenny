# 백준 16928번. 뱀과 사다리 게임

# 보드판: 10x10, 1~100번.
# 주사위 던져 i -> i + k만큼 이동.
# 사다리면 위로 올라감. (커짐)
# 뱀이면 아래로 내려감. (작아짐)

# 구하는 것: 1번 칸에서 시작해 100번 칸에 도착하기 위해 주사위를 굴려야 하는 최소 횟수
# 한 번에 1~6칸 이동.

# dp인줄 알고 풀었는데, 풀다보니까 뱀때문에 dp는 아닌 것 같다. (뱀 때문에 앞선 값이 바뀌면 그 뒤로 다시 계산해야 해서)

# bfs
# i에 있을 때 이동할 수 있는 칸: i+1~i+6, i-뱀, i+사다리

from collections import deque

N, M = map(int, input().split())
board = [i for i in range(101)]
for _ in range(N):
    x, y = map(int, input().split())
    board[x] = y
for _ in range(M):
    u, v = map(int, input().split())
    board[u] = v

# visited
# 거리: queue에 같이 넣기.
queue = deque([(1, 0)])
visited = [False for _ in range(101)]
while queue:
    i, cnt = queue.popleft()
    # visited[i + k] = True
    if i == 100:
        print(cnt)
        break

    nxt = []
    for k in range(1, 7):
        if i + k <= 100 and not visited[i+k]:
            visited[i + k] = True # 놓친 부분. 큐에서 뽑을 때가 아니라 넣을 때 방문 처리. -> 탐색 수 및 시간 감소
            nxt.append((board[i + k], cnt + 1))
    nxt.sort(key=lambda x: -x[0]) # 정렬: 더 멀리 가는 경우를 먼저 탐색함
    queue.extend(nxt)
    # 정렬: 탐색 수가 감소할 수 있음. O(6log6)이지만 불필요한 연산이긴 함.

    # for k in range(1, 7):
    #     if i + k <= 100 and not visited[i+k]:
    #         visited[i + k] = True
    #         queue.append((board[i + k], cnt + 1))
    # 정렬하지 않으면
    # - 방문 처리를 큐에 넣을 때 해야 함.
    # - 그렇지 않으면, 의미 없는 값들(이전에 방문 처리됨, 뱀 타고 내려감)이 큐에 들어가서 탐색 수가 많아짐
