# 문제 링크: https://www.acmicpc.net/problem/2522

N = int(input())

for i in range(-N + 1, N):
    print(' ' * abs(i) + '*' * (N - abs(i)))
