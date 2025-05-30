# 백준 2003번. 수들의 합 2
# 10 5 (길이가 10, 합이 5)
# 1 2 3 4 2 5 3 1 1 2
# -> 2 3, 5, 3 1 1
# 바로 생각나는 방법: 길이를 1~N 늘려가며 순회하기
# 중간에 M보다 합이 커지면 패스하기 -> 백트래킹?
# N 최대: 10,000
# M 최대: 300,000,000
# 최악의 경우: N = 300,000,000 이고 모두 1로 이루어져 있음. M = 300,000,000 -> 시간 복잡도: O(N^2)

N, M = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
for i in range(N):
    sum = 0
    for j in range(i, N):
        sum += arr[j]
        if sum >= M:
            if sum == M:
                answer += 1
            break

print(answer)
