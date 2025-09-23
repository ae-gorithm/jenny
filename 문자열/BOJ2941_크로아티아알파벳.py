# 백준 2941번. 크로아티아 알파벳
"""
문자열 문제

크로아티아 알파벳: c=, c-, dz=, d-, lj, nj, s=, z=, 나머지 알파벳 a~z
단어가 주어졌을 때 크로아티아 알파벳이 몇 개인지 출력

체크 포인트
- 파이썬 배열 슬라이싱 시간 복잡도: 슬라이스 길이가 k라면 O(k)이다. 파이썬 리스트 슬라이싱 연산은 새로운 리스트 객체를 만들어 원소들을 복사한다.
- len(container)는 O(1). 지역 변수 캐싱과 직접 호출과 속도 차이가 거의 없지만, 캐싱은 가독성이나 한 번만 쓰겠다는 의도를 드러내는 용도로 씀.
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
