# 문제 링크: https://www.acmicpc.net/problem/6783

import sys
input = sys.stdin.readline

s = ''.join(input() for _ in range(int(input()))).lower()

print('English' if s.count('t') > s.count('s') else 'French')
