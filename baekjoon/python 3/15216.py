# 문제 링크: https://www.acmicpc.net/problem/15216

h, w, n = map(int, input().split())
x = list(map(int, input().split()))

c = 0
while h > 0 and c < w and x:
    c += x.pop(0)
    if c == w:
        h -= 1
        c = 0

print(['YES', 'NO'][h > 0])
