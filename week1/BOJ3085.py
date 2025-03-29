# 제목: BOJ3085 사탕 게임
# 문제: 색이 다른 인접한 두칸을 교환한다 -> 같은 색이 연속되는 길이의 최댓값을 찾는다.
# 아이디어:
# 두 칸을 바꾸는 모든 경우에 대해, 교환 후 긴 영역을 찾는 과정을 반복한다.
# 매 경우마다, board는 원상복귀 해주어야 함
# 중복을 줄이기 위한 방법:
# - 처음 board에서 가장 긴 길이를 구한다.
# - 교환 후, 바뀐 열/행에 대해서만 최대 연속 길이를 계산한다.

# 전체 보드 안에서 최대 연속 길이 찾는 함수
def count_in_board():
    longest = 0
    for i in range(n):
        row_cnt, col_cnt = 1, 1
        for j in range(1, n): # 가로 탐색
            if board[i][j] == board[i][j-1]:
                row_cnt += 1
            else:
                row_cnt = 1
        for j in range(1, n): # 세로 탐색
            if board[j][i] == board[j-1][i]:
                col_cnt += 1
            else:
                col_cnt = 1
        longest = max(longest, row_cnt, col_cnt)
    return longest

# 한 라인 안에서 최대 연속 길이 찾는 함수
def count(x, row):
    longest = 0
    cnt = 1
    if row: # 가로 행에서 계산
        for k in range(1, n):
            if board[x][k] == board[x][k-1]:
                cnt += 1
            else:
                cnt = 1
            longest = max(longest, cnt)
    else: # 세로 열에서 계산
        for k in range(1, n):
            if board[k][x] == board[k-1][x]:
                cnt += 1
            else:
                cnt = 1
            longest = max(longest, cnt)
    return longest


n = int(input())
board = [list(input()) for _ in range(n)]
answer = count_in_board()

for i in range(n):
    for j in range(n-1):
        # 가로 교환
        if board[i][j] != board[i][j+1]:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            answer = max(answer, count(i, True), count(j, False), count(j + 1, False))
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        # 세로 교환
        if board[j][i] != board[j+1][i]:
            board[j][i], board[j+1][i] = board[j+1][i], board[j][i]
            answer = max(answer, count(j, True), count(j+1, True), count(i, False))
            board[j][i], board[j+1][i] = board[j+1][i], board[j][i]

print(answer)