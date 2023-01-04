# 문제 링크: https://www.acmicpc.net/problem/10902

f = P = max_s = 0
for i in range(1, int(input()) + 1):
    t, s = map(int, input().split())
    if s > max_s:
        f = i
        P = t + (f - 1) * 20 if s > 0 else 0
        max_s = s

print(P)
