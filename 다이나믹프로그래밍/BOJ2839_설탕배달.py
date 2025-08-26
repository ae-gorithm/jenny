# 백준 2839번. 설탕 배달
"""
DP로 풀기 -> 마지막 숫자에서 차이 찾기
dp[n] = min(dp[n-3], dp[n-5]) + 1 (단, dp[n-3] 또는 dp[n-5]가 -1이 아닌 경우에만)

초기값 구하기
dp[1]=-1
dp[2]=-1
dp[3]=1
dp[4]=-1
dp[5]=1
"""

n = int(input())
dp = [0, -1, -1, 1, -1, 1]
if n <= 5:
    print(dp[n])
else:
    for i in range(6, n+1):
        if dp[i-3] == -1 and dp[i-5] == -1:
            dp.append(-1)
        elif dp[i-3] > 0 and dp[i-5] > 0:
            dp.append(min(dp[i-3], dp[i-5]) + 1)
        else:
            dp.append(max(dp[i-3], dp[i-5]) + 1)
    print(dp[n])
