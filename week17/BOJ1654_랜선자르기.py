# 백준 1654번. 랜선 자르기

# K개 랜선의 길이를 잘라서 N개의 같은 길이의 랜선으로 만든다. N개를 만드는 최대 길이.
# 파라메트릭 서치.
# 최소: 1, 최대: 제일 긴 랜선 길이(보다 커질 수 없으므로)
# 이진 탐색을 해서 최대 길이를 찾는다.

K, N = map(int, input().split())
arr = []
for _ in range(K):
    arr.append(int(input()))

left = 1
right = max(arr)
answer = 0
while left <= right:
    mid = (left + right) // 2 # zero division 주의. 현재는 left가 1부터 시작하므로 발생 가능성 없음. (mid 최소 1)
    count = 0
    for i in range(K):
        count += arr[i] // mid
    if count >= N:
        left = mid + 1
        answer = max(answer, mid)
    else:
        right = mid - 1
print(answer)
