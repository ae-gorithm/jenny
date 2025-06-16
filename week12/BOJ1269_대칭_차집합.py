# 백준 1269번. 대칭 차집합
# 두 집합이 있을 때, 두 집합의 대칭 차집합의 원소의 개수를 구한다.
# 대칭 차집합: (A-B)와 (B-A)의 합집합
# A에서 B에 있는 것들을 빼고, B에서 A에 있는 것들을 뺌. -> 둘의 합집합 - 교집합 -> 두 개 공통인 것 뺀 나머지
# 개수만 구하는 거면, A크기 + B크기 - 교집합크기*2

a, b = map(int, input().split())
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

setAB = set(arrA + arrB)
n = len(arrA) + len(arrB) - len(setAB)
answer = len(arrA) + len(arrB) - 2*n
print(answer)
