# 문제 링크: https://www.acmicpc.net/problem/9891

import sys
input = sys.stdin.readline

n, r = int(input()), []
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    r.append(sorted([x2 - x1, y2 - y1]))

print(sum(
    (r[i][0] < r[j][0] or r[i][1] < r[j][1]) and (r[i][0] > r[j][0] or r[i][1] > r[j][1])
    for i in range(n - 1)
    for j in range(i + 1, n)
))
