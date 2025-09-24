# 백준 9093번. 단어 뒤집기
"""
문장 속 각 단어들을 뒤집는다.

"""

# reverse 직접 작성해보기
# 뒤에서부터 순회하면서 문자열에 덧셈 연산하는 방법
# def reverse(old):
#     new = ""
#     for i in range(len(old)):
#         new += old[-i-1]
#     return new

# T = int(input())
# for _ in range(T):
#     s = input().split()
#     for i, w in enumerate(s):
#         # 뒤집기
#         s[i] = reverse(w)
#
#     # 리스트를 문자열로 바꿔 출력 -> 문자열 그대로 하는 방법 없을까?
#     # for w in s:
#     #     print(w, end=" ")
#     print(' '.join(s))

T = int(input())
for _ in range(T):
    s = input().split()
    print(' '.join(w[::-1] for w in s))