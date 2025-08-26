# 백준 1463번. 1로 만들기
"""
연산: X/3, X/2, X-1
연산을 통해 1로 만든다.
dp[n] = min(dp[x/3], dp[x/2], dp[x-1]) + 1

초기값
dp[1] = 0
dp[2] = 1
dp[3] = 1
"""

n = int(input())
dp = [0] * (n+1)
for i in range(2, n+1):
    arr = [dp[i-1]]
    if i % 3 == 0:
        arr.append(dp[i//3])
    if i % 2 == 0:
        arr.append(dp[i//2])
    dp[n] = min(arr)+1
print(dp[n])
