# 백준 1010번. 다리 놓기
"""
왼쪽 N개, 오른쪽 M개. 겹치지 않게 점을 잇는 경우의 수.
오른쪽 M개 중 N개를 고르면 됨. mCn (조합)

-> DP로 푸는 법?
DP는 마지막 한 스텝을 잘 생각해야 한다.
m개 중 n개가 선택되려면 m까지 정확히 n개가 무조건 선택되어야 함.
1. m-1번 점까지 n개 이어진 경우: m번째 점을 고르지 않는 경우
2. m-1번 점까지 n-1개 이어진 경우: im째 점을 고르는 경우
dp[i][j]: 오른쪽 i개 점 중 j개가 선택되는 경우의 수.
dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

삼각형 ◥ 부분은 0.

=> 조합을 수식 말고 DP로 푸는 법 !
"""
dp = [[0] * 31 for _ in range(31)] # dp[i][j] = i개 중 j개를 고르는 경우의 수

for i in range(31):
    dp[i][0] = 1     # iC0 = 1
    dp[i][i] = 1     # iCi = 1

for i in range(1, 31):
    for j in range(1, i):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    print(dp[m][n])
