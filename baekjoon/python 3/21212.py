# 문제 링크: https://www.acmicpc.net/problem/21212

cakes = 10000
for _ in range(int(input())):
    a, b = map(int, input().split())
    cakes = min(b // a, cakes)

print(cakes)
