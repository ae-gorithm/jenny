# 백준 4779번. 칸토어 집합

while True:
    try:
        N = int(input())

        answer = '-'
        for i in range(0, N):
            substr = answer
            answer = substr + ' ' * (3**i) + substr
        print(answer)
    except:
        break