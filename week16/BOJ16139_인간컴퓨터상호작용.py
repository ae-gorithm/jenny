# 백준 16139번. 인간-컴퓨터 상호작용

# 특정 문자열 S의 구간 [l, r] 사이에 특정 알파벳 a가 몇 번 나타나는지 구한다.
# 같은 문자열 S을 두고 질문을 q번 한다.
# 태스크 1: S 길이 <= 2000, q <= 2000
# 태스크 2: S 길이 <= 200000, q <= 200000
# 중복 결과를 저장해야 함. -> 이중 for문이면 S * q = 4백억

# 최악의 경우:
# S = "bbbbbbb...b", q = 2000000, a = "b", l = 0, r = 200000
import sys
input = sys.stdin.readline

S = input().strip()
alphabet = [[0 for i in range(len(S) + 1)] for j in range(26)]
alphabet[ord(S[0]) - 97][1] = 1
for i in range(1, len(S)): # 최악의 수: 200,000*26
    idx = ord(S[i]) - 97
    for j in range(26):
        alphabet[j][i + 1] = alphabet[j][i] # 시간초과
        # -> pypy3은 sys.stdin.readline로 해결 가능. python3는 불가능
    alphabet[idx][i + 1] += 1

q = int(input())
for _ in range(q):
    a, l, r = input().split()
    ord_a = ord(a) - 97
    cnt = alphabet[ord_a][int(r)+1] - alphabet[ord_a][int(l)]
    print(cnt)
