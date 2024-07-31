# 문제 링크: https://www.acmicpc.net/problem/10501

from sys import stdin

lines = [len(s) for s in stdin]
n = max(lines)

print(sum((n - m)**2 for m in lines[:-1]))
