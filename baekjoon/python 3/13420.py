# 문제 링크: https://www.acmicpc.net/problem/13420

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    print(['wrong answer', 'correct'][eval(input().replace('=', '=='))])
