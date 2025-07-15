# 백준 2096번. 내려가기

# 줄이 N개이고, 각 줄에는 숫자(0~9)가 세 개 적혀있다.
# 1번 줄 부터 N번 줄까지 숫자를 선택하며 내려간다.
# (i, j) 에서 갈 수 있는 숫자는 (i+1, j-1), (i+1, j), (i+1, j+1) 중 하나다.

# 최대 점수와 최소 점수를 구한다. -> 다 해봐야 함.
# -> DP로 풀 수 있을 것 같다. (i, j)까지의 최소, 최대를 저장.

dir = [[0, 1], [-1, 0, 1], [-1, 0]]

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

max_arr = [arr[0][0], arr[0][1], arr[0][2]] # j번째 열의 최대 점수를 저장.
min_arr = [arr[0][0], arr[0][1], arr[0][2]] # j번째 열의 최솟 점수를 저장.
for i in range(1, N):
    max_temp = []
    min_temp = []
    for j in range(3):
        max_num = 0
        min_num = 900000
        for k in dir[j]:
            # 각 자리에서 가질 수 있는 최대, 최소 점수를 계산
            max_num = max(max_num, max_arr[j + k])
            min_num = min(min_num, min_arr[j + k])
        max_temp.append(max_num + arr[i][j])
        min_temp.append(min_num + arr[i][j])
    max_arr = max_temp
    min_arr = min_temp

print(max(max_arr), min(min_arr))
