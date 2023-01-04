# 문제 링크: https://www.acmicpc.net/problem/10902

max_s = P = 0
for i in range(1, int(input()) + 1):
    t, s = map(int, input().split())
    if s > max_s:
        max_s = s
        P = t + (i - 1) * 20 if s > 0 else 0

print(P)
