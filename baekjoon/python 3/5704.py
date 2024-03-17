# 문제 링크: https://www.acmicpc.net/problem/5704

import sys
input = sys.stdin.readline

while (s := input().strip()) != '*':
    s = set(s)
    s.discard(' ')

    print('Y' if len(s) == 26 else 'N')
