# 문제 링크: https://www.acmicpc.net/problem/2605

n = []
input()
for i, j in enumerate(map(int, input().split())):
    n.insert(i - j, i + 1)

print(*n)
