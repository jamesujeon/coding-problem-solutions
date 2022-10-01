# 문제 링크: https://www.acmicpc.net/problem/5063

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    r, e, c = map(int, input().split())

    if r < e - c:
        print('advertise')
    elif r > e - c:
        print('do not advertise')
    else:
        print('does not matter')
