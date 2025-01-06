# 문제 링크: https://www.acmicpc.net/problem/16019

d = [0] + list(map(int, input().split()))
for i in range(4):
    d[i + 1] += d[i]

for i in range(5):
    print(*[abs(d[i] - d[j]) for j in range(5)])
