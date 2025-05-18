# 백준 2839번. 설탕 배달

def find(n):
    x = n // 5
    for i in range(x, -1, -1):
        if (n - 5 * i) % 3 == 0:
            return i + (n - 5 * i) // 3
    return -1

N = int(input())
print(find(N))