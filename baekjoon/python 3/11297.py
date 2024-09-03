# 문제 링크: https://www.acmicpc.net/problem/11297

import sys
input = sys.stdin.readline

while (s := input().strip()) != '0 0 0':
    s = sum(map(int, s.split())) % 25 + 1
    print(''.join(chr((ord(c) - 97 - s) % 26 + 97) if c.isalpha() else c for c in input().strip()))
