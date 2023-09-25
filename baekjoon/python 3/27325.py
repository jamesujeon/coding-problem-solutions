# 문제 링크: https://www.acmicpc.net/problem/27325

input()
r, x = 0, 1
for d in input():
    x = max(x - 1, 1) if d == 'L' else min(x + 1, 3)
    if x == 3:
        r += 1

print(r)
