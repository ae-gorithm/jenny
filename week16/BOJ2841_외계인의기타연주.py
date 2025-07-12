# 백준 2841번. 외계인의 기타 연주

# 6줄 -> 프렛 1~P번
# 가장 높은 프렛의 음이 발생한다. -> 음이 내려가면 그 위의 손가락을 다 떼야하고, 음이 올라가면 유지해도 된다.
# 다른 줄이 눌려 있어도 음이 난다.

# 자료 구조: stack, 각 음 별로 리스트가 있어야.

N, P = map(int, input().split()) # 멜로디 N개, 프렛 P개
arr = [[] for _ in range(7)]
answer = 0
for _ in range(N):
    l, p = map(int, input().split())
    if len(arr[l]) == 0:
        arr[l].append(p)
        answer += 1
    else:
        top = arr[l][-1] # 맨 마지막 프렛
        if top == p: # 같은 프렛인 경우
            pass
        elif top > p: # 큰 프렛인 경우
            while top > p:
                arr[l].pop()
                answer += 1
                if len(arr[l]) == 0:
                    break
                else:
                    top = arr[l][-1]
            if top == p:
                pass
            else:
                arr[l].append(p)
                answer += 1
        else: # 작은 프렛인 경우
            arr[l].append(p)
            answer += 1

print(answer)
