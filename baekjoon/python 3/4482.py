# 문제 링크: https://www.acmicpc.net/problem/4482

for i in range(1, int(input()) + 1):
    n = int(input())

    print(f'{i}: {n} {n * (n + 1) * (n + 2) // 6}')
