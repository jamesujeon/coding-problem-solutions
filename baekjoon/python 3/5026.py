# 문제 링크: https://www.acmicpc.net/problem/5026

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().strip()

    print(sum(map(int, s.split('+'))) if s != 'P=NP' else 'skipped')
