# 백준 2941번. 크로아티아 알파벳
"""
문자열 문제

크로아티아 알파벳: c=, c-, dz=, d-, lj, nj, s=, z=, 나머지 알파벳 a~z
단어가 주어졌을 때 크로아티아 알파벳이 몇 개인지 출력

"""

word = input()
alpha = ["c=", "c-", "d-", "lj", "nj", "s=", "z="]

answer = 0
i = 0
while i < len(word):
    if i+2 < len(word) and word[i:i+3] == "dz=":
        i += 3
    elif i+1 < len(word) and word[i:i+2] in alpha:
        i += 2
    else:
        i += 1
    answer += 1
print(answer)
