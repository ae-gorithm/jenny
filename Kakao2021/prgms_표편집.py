"""
현재 선택된 행을 저장. -> k
최근 삭제 복구 -> 스택 필요
삭제는 OX로 표현.

효율성
1. 행 이동을 최대한 한 번에 한다. -> 여전히 시간초과 (1개만 통과)
2. 행 이동 시간복잡도를 줄인다. 반복문 없애는 방법? 01010 비트로 표현하고 비트 연산으로 한다면?

"""


def solution(n, k, cmd):
    rows = [True] * n  # 행의 삭제여부
    deleted = []  # 삭제된 행들의 인덱스
    last = n - 1  # 맨 마지막 행 인덱스

    def move(distance, k):
        if distance < 0:
            direction = -1
            distance *= -1
        else:
            direction = 1

        while distance > 0:
            k = k + direction
            if rows[k]:
                distance -= 1
        return k

    moving = 0
    for c in cmd:
        task = list(c.split())

        # U: 위로 X칸 이동
        if task[0] == 'U':
            moving -= int(task[1])

        # D: 아래로 X칸 이동
        elif task[0] == 'D':
            moving += int(task[1])

        else:
            # 한 번에 이동 처리
            if moving != 0:
                k = move(moving, k)
                moving = 0

            # C: 현재 행 삭제
            if task[0] == 'C':
                rows[k] = False
                deleted.append(k)
                if k == last:
                    k = move(-1, k)
                    last = k
                else:
                    k = move(1, k)

            # Z: 삭제된 행 복구
            else:
                x = deleted.pop()
                rows[x] = True
                if x > last:
                    last = x

    answer = ''
    for x in rows:
        answer = answer + 'O' if x else answer + 'X'
    return answer


def main():
    print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
    print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))

main()
