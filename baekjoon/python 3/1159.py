# 문제 링크: https://www.acmicpc.net/problem/1159

import sys
input = sys.stdin.readline

names = [input()[0] for _ in range(int(input()))]

result = ''.join(sorted([name for name in set(names) if names.count(name) >= 5]))

print(result or 'PREDAJA')
