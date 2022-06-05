# 문제 링크: https://www.acmicpc.net/problem/1173

N, m, M, T, R = map(int, input().split())

if m + T > M:
    print(-1)
    exit(0)

minutes = 0
X = m
while N > 0:
    if X + T <= M:
        X += T
        N -= 1
    else:
        X = max(X - R, m)
    minutes += 1

print(minutes)
