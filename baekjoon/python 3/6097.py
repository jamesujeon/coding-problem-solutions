# 문제 링크: https://www.acmicpc.net/problem/6097

N, P = map(int, input().split())

d = str(N**P)
for i in range(0, len(d), 70):
    print(d[i:i + 70])
