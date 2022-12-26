# 문제 링크: https://www.acmicpc.net/problem/10992

N = int(input())

print(' ' * (N - 1) + '*')
for i in range(1, N - 1):
    print(' ' * (N - i - 1) + '*' + ' ' * (i * 2 - 1) + '*')
if N > 1:
    print('*' * (N * 2 - 1))
