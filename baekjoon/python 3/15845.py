# 문제 링크: https://www.acmicpc.net/problem/15845

n, m = map(int, input().split())
t = list(map(int, input().split()))
c = []
for i in range(n):
    s = list(map(int, input().split()))
    c.append((-sum(s[j] == t[j] for j in range(m)), i))

print(sorted(c)[0][1] + 1)
