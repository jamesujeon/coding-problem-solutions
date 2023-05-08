# 문제 링크: https://www.acmicpc.net/problem/22150

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    t = list(map(int, input().split()))
    n, lr = t[0], t[1:]

    print('no' if n * n == sum(lr) else 'yes')
