# 문제 링크: https://www.acmicpc.net/problem/5698

import sys
input = sys.stdin.readline

while (s := input().lower().strip()) != '*':
    print('NY'[all(w[0] == s[0] for w in s.split())])
