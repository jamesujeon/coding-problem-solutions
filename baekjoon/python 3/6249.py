# 문제 링크: https://www.acmicpc.net/problem/6249

n, p, h = map(int, input().split())

for _ in range(n):
    d = int(input())
    if d < p:
        print(f'NTV: Dollar dropped by {p - d} Oshloobs')
    elif d > h:
        print(f'BBTV: Dollar reached {d} Oshloobs, A record!')
        h = d
    p = d
