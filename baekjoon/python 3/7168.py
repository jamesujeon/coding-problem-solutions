# 문제 링크: https://www.acmicpc.net/problem/7168

N, M = map(int, input().split())
d = [input() for _ in range(N)]

for i in range(N):
    s = [len(s) for s in d[i].split('.') if s]
    print(*(s if s else [0]))

for j in range(M):
    s = [len(s) for s in ''.join(d[i][j] for i in range(N)).split('.') if s]
    print(*(s if s else [0]))
