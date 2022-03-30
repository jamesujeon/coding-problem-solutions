# 문제 링크: https://www.acmicpc.net/problem/2445

N = int(input())

for i in range(1, N + 1):
    print('*' * i + ' ' * (N - i) * 2 + '*' * i)
for i in range(1, N):
    print('*' * (N - i) + ' ' * i * 2 + '*' * (N - i))
