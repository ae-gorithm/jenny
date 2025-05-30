# 백준 2003번. 수의 합 2
# 투 포인터 방식으로 풀기
# 시간 복잡도 O(N): 각 요소를 start, end에서 최대 한 번씩만 방문
# start, end 둘 다 0에서 시작해서 각각 이동시키며 구간합이 M인 부분을 찾는다.
# end를 오른쪽으로 옮기며 수를 더해가다가 M 이상이 되면 start를 오른쪽으로 옮긴다. 이를 반복해서 구간을 계속 옮겨나가는 방식.

N, M = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 0
total = 0
answer = 0

while True:
    if total >= M:
        total -= arr[start]
        start += 1
    elif end == N:
        break
    else:
        total += arr[end]
        end += 1

    if total == M:
        answer += 1

print(answer)
