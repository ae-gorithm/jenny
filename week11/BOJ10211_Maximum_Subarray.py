# 백준 10211번. Maximum Subarray
# 투 포인터로 풀려고 했는데, 결국 브루트포스와 동일
import sys

def maximum_subarray(n, arr):
    answer = sys.maxsize * (-1)
    for i in range(n):
        start, end = i, i
        sum = 0
        while end < n:
            sum += arr[end]
            end += 1
            answer = max(sum, answer)
    return answer

T = int(input())
for _ in range(T):
    N = int(input())
    test_arr = list(map(int, input().split()))
    print(maximum_subarray(N, test_arr))
