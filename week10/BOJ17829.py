# 백준 17829번. 222-풀링
# 222-풀링이란 행렬을 2x2로 나누어서 그 중 두 번째로 큰 수만 남기는 과정을 반복하며, 마지막에 남는 수를 구하는 것.

# 2x2에 들어가는 위치의 인덱스를 일반화해보자
# i, j / i+1, j / i, j+1 / i+1, j+1
# i, j는 2*k (k=0 ~ N/2)
# 있는 그대로 풀어보기

def second(arr):
    return sorted(arr)[2]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

while True:
    if len(arr) == 1:
        break

    new_arr = [[0] * (N//2) for _ in range(N//2)]
    # new_arr = [[0] * (N//2)] * (N//2)
    for i in range(0, N, 2):
        for j in range(0, N, 2):
            result = second([arr[i][j], arr[i+1][j], arr[i][j+1], arr[i+1][j+1]])
            new_arr[i//2][j//2] = result
    N = N//2
    arr = new_arr

print(arr[0][0])