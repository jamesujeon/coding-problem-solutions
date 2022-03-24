# 문제 링크: https://www.acmicpc.net/problem/2443

N = int(input())

for i in range(N):
    print(' ' * i + '*' * ((N - i) * 2 - 1))
