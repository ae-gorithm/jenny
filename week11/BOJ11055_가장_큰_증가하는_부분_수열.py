# 백준 11055번. 가장 큰 증가하는 부분 수열
# 문제: 수열 A가 주어졌을 때, 그 수열의 증가하는 부분 수열 중 합이 가장 큰 것을 구한다.
# 이전에 부분수열의 최대 합을 구하는 문제 + 부분수열이 증가하는 조건이 추가됨

# 포인터를 옮기다가 뒤의 수가 앞의 수보다 작아지면, 뒤의 수에서 포인터 재설정 -> X. 연속하지 않아도 됨.

# 부분 수열 -> 꼭 연속적이지 않아도 된다.
# 해결 방법: DP

N = int(input())
arr = list(map(int, input().split()))

dp = [arr[i] for i in range(N)]
for i in range(N):
    for j in range(0, i): # j < i
        if arr[j] < arr[i]: # 증가하는 부분 수열
            dp[i] = max(dp[j] + arr[i], dp[i])

# print(dp)
print(max(dp))
