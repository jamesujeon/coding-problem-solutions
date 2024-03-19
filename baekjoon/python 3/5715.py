# 문제 링크: https://www.acmicpc.net/problem/5715

import sys
input = sys.stdin.readline

d = {'W': 64, 'H': 32, 'Q': 16, 'E': 8, 'S': 4, 'T': 2, 'X': 1}

while (s := input().strip()) != '*':
    print(sum(sum(d[i] for i in n) == 64 for n in s[1:-1].split('/')))
