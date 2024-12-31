# 문제 링크: https://www.acmicpc.net/problem/15814

s, t = list(input()), int(input())
for _ in range(t):
    a, b = map(int, input().split())
    s[a], s[b] = s[b], s[a]

print(''.join(s))
