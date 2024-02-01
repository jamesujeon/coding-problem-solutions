# 문제 링크: https://www.acmicpc.net/problem/4581

import sys
input = sys.stdin.readline

while (s := input().strip()) != '#':
    if s.count('A') * 2 >= len(s):
        print('need quorum')
    elif s.count('Y') > s.count('N'):
        print('yes')
    elif s.count('Y') < s.count('N'):
        print('no')
    else:
        print('tie')
