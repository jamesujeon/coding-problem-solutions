# 문제 링크: https://www.acmicpc.net/problem/6502

import sys
input = sys.stdin.readline

i = 1
while (s := input().strip()) != '0':
    r, w, l = map(int, s.split())

    print(f"Pizza {i} {'fits' if w * w + l * l <= r * r * 4 else 'does not fit'} on the table.")
    i += 1
