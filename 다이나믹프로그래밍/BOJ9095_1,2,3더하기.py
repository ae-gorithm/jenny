# 백준 9095번. 1,2,3 더하기
"""
정수 n을 1,2,3의 합으로 나타내는 방법의 수를 구한다. (경우의 수)
자리가 다르면 서로 다른 경우의 수

다이나믹 프로그래밍
점화식 구하기: 마지막에 더하는 수로 경우의 수 나누기
dp[n] = dp[n-1] + dp[n-2] + dp[n-3]

dp[1]=1 : 1
dp[2]=2 : 11, 2
dp[3]=4 : 111, 21, 12, 3
dp[4]=7 =1+2+4 (예제와 동일)
dp[5]=13 =2+4+7
dp[6]=24 =4+7+13
dp[7]=44 (예제와 동일)
dp[8]=81
dp[9]=149
dp[10]=274 (예제와 동일)
"""

T=int(input())
testcase = []
for _ in range(T):
    testcase.append(int(input()))
max_case = max(testcase) # dp[max_case] 까지 구하자.

# dp 구하기
dp = [0, 1, 2, 4]
for i in range(4, max_case+1):
    dp.append(dp[i-1] + dp[i-2] + dp[i-3])

# 출력
for t in range(T):
    print(dp[testcase[t]])
