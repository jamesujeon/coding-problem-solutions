# 문제 링크: https://www.acmicpc.net/problem/2562

n = [int(input()) for _ in range(9)]
m = max(n)
print(m)
print(n.index(m) + 1)