# 백준 1966번. 프린터 큐
# FIFO가 아닌, 중요도에 따라 출력한다.
# 현재 가장 앞에 있는 문서의 '중요도'를 확인한 후, 가장 높을 경우에만 인쇄. 아니면 가장 뒤에 재배치하는 방식.
# 어떤 한 문서가 몇 번째로 인쇄되는지 알아낸다. -> 전체 횟수를 셀 count 변수가 필요하다.

from collections import deque

def printer(n, m, priority):
    queue = deque([_ for _ in range(n)])
    count = 0
    max_p = max(priority)

    while queue:
        target = queue.popleft()
        if priority[target] >= max_p: # 인쇄
            count += 1
            if target == m:
                return count
            priority[target] = 0
            max_p = max(priority)
        else:
            queue.append(target)

    return -1


def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        priority = list(map(int, input().split()))
        print(printer(n, m, priority))

main()