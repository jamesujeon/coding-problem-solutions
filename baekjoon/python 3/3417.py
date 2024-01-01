# 문제 링크: https://www.acmicpc.net/problem/3417

import sys
input = sys.stdin.readline

while True:
    k = input().strip()
    if k == '0':
        break

    p = input().strip()
    print(''.join(chr((ord(p[i]) + ord(k[i % len(k)]) - 129) % 26 + 65) for i in range(len(p))))
