# 문제 링크: https://www.acmicpc.net/problem/14624

N = int(input())
if N % 2:
    print('*' * N)
    print(' ' * (N // 2) + '*')
    for i in range(N // 2):
        print(' ' * (N // 2 - i - 1) + '*' + ' ' * (i * 2 + 1) + '*')
else:
    print('I LOVE CBNU')
