# 문제 링크: https://www.acmicpc.net/problem/2445

N = int(input())

for i in range(-N + 1, N):
    print('*' * (N - abs(i)) + ' ' * abs(i) * 2 + '*' * (N - abs(i)))
