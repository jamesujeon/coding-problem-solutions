# 문제 링크: https://www.acmicpc.net/problem/28417

import sys
input = sys.stdin.readline

result = 0
for _ in range(int(input())):
    s = list(map(int, input().split()))
    result = max(max(s[:2]) + sum(sorted(s[2:])[-2:]), result)

print(result)
