# 문제 링크: https://www.acmicpc.net/problem/11149

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    print(''.join(
        chr(c + 97) if (c := sum(ord(c) - 97 for c in w) % 27) < 26 else ' '
        for w in input().split())
    )
