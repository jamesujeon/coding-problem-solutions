# 문제 링크: https://www.acmicpc.net/problem/26510

for N in map(int, input().split()):
    for i in range(N - 1):
        print(' ' * i + '*' + ' ' * ((N - i) * 2 - 3) + '*')
    print(' ' * (N - 1) + '*')
