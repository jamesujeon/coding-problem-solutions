# 문제 링크: https://www.acmicpc.net/problem/14551

N, M = map(int, input().split())
c = 1
for _ in range(N):
    c *= max(int(input()), 1)

print(c % M)
