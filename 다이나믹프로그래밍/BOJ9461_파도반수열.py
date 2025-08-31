# 백준 9461번. 파도반 수열
"""
규칙: P(N) = P(N-2) + P(N-3)
초기값: P(1)=1, P(2)=1, P(3)=1
점화식 -> DP로 풀기
"""

T = int(input())
testcase = [int(input()) for _ in range(T)]
max_case = max(testcase)

P = [1] * max_case
for i in range(3, max_case):
    P[i] = P[i-2] + P[i-3]

for t in testcase:
    print(P[t-1])
