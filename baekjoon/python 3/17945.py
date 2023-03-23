# 문제 링크: https://www.acmicpc.net/problem/17945

A, B = map(int, input().split())

x1 = -1 * A + (A**2 - B)**.5
x2 = -1 * A - (A**2 - B)**.5

print(' '.join(map(str, map(int, sorted({x1, x2})))))
