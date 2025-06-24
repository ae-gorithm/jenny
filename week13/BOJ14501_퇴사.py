# 백준 14501번. 퇴사
# 파이썬으로 풀고 나서 Java로 풀어보기

# 목표: N일 동안 최대한 많은 상담을 한다.
# 조건: 하루에 상담 하나만 가능. 상담은 여러 일. 상담별 가격이 다름.
# 수익이 최대가 되도록 상담을 선택해야 함.

# 모든 경우의 수를 다 구하는 방법. 1일부터 시작해 상담 하고 안하고 선택. (쓴맛,신맛 문제랑 같은 방법으로)

def find(i, p):
    global answer
    if i >= N:
        answer = max(p, answer)
        return
    if i + arr[i][0] <= N:
        find(i + arr[i][0], p + arr[i][1]) # 선택하는 경우
    find(i + 1, p) # 선택하지 않는 경우

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = 0
find(0, 0)
print(answer)
