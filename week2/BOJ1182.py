# 백준 1182번. 부분수열의 합
# 문제: 부분 수열의 합이 S가 되는 경우의 수를 구한다.
# 아이디어: 백트래킹 적용하는 법?

from itertools import combinations

n, s = map(int, input().split())
sequence = list(map(int, input().split()))
sequence.sort()

answer = 0

for i in range(1, n + 1):
    for comb in combinations(sequence, i):
        print(comb)
        si = sum(comb)
        if si == s:
            answer += 1

print(answer)
