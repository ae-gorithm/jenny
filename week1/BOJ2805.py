# 백준 2805번. 나무 자르기
# 나무를 가져가기 위한 절단기 높이 h의 최댓값 구하기.
# 이진탐색
# 높이를 조절해가며 최적의 값을 찾는다.
# - 이진탐색을 통해 계산할 높이 개수를 줄이는 것이 포인트
# - 총합이 m 이상이면 h를 더 높여보면서, 조건을 만족하는 최대 h값을 찾는다.
# - 총합이 m 미만이면 h를 더 낮춰서 찾는다.

n, m = map(int, input().split())
tree = list(map(int, input().split()))

def cut_tree(h):
    sum = 0
    for i in tree:
        if i - h > 0:
            sum += (i - h)
    return sum

answer = 0

low = 0
high = max(tree) - 1
while low <= high:
    h = (low + high) // 2
    cut_amount = cut_tree(h)
    if cut_amount >= m:
        answer = h
        low = h + 1
    else:
        high = h - 1

print(answer)