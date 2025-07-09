# 백준 1535번. 안녕 ...

# 1~N번까지, 인사: 체력 -L[i], 기쁨 +J[i]
# 체력 >=0, 기쁨 최대
# 초기 체력: 100, 초기 기쁨: 0

# 다 해봐야 하나..?
# 포함/미포함 재귀로?

answer = 0
def find(i, life, joy):
    global answer
    if life > 0:
        answer = max(answer, joy)

    if i + 1 < N:
        find(i + 1, life, joy) # i+1번째 사람 건너뜀
        find(i + 1, life - L[i+1], joy + J[i+1]) # i+1번째 사람에게 인사

N = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))

find(-1, 100, 0)
print(answer)
