# 백준 2003번. 수들의 합 2
# 누적합 방식으로 풀기
# 시간 복잡도: O(N^2)

N, M = map(int, input().split())
arr = list(map(int, input().split()))
prefix_arr = [0] * (N + 1)

for i in range(N):
    prefix_arr[i + 1] += prefix_arr[i] + arr[i]

answer = 0
for i in range(N):
    for j in range(i + 1, N + 1):
        if prefix_arr[j] - prefix_arr[i] >= M:
            if prefix_arr[j] - prefix_arr[i] == M:
                answer += 1
            break

print(answer)
