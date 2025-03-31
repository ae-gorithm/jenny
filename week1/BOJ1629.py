# 백준 1529번. 곱셈
# 문제: 자연수 A를 B번 곱한 수를 C로 나눈 나머지를 출력하라.
# 알고리즘: 분할 정복
# - 중복되는 부분은 한 번만 계산한다.
# - 반복마다 C로 나누어줘서 크기를 줄인다.

def calc(A, B, C):
    if B == 0:
        return 1
    num = calc(A, B // 2, C)
    if B % 2 == 0:
        return num * num % C
    else:
        return num * num * A % C

a, b, c = map(int, input().split())
print(calc(a, b, c))