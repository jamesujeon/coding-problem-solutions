# 문제 링크: https://www.acmicpc.net/problem/10990

N = int(input())

print(' ' * (N - 1) + '*')
for i in range(N - 1):
    print(' ' * (N - i - 2) + '*' + ' ' * (i * 2 + 1) + '*')
