# 문제 링크: https://www.acmicpc.net/problem/25812

n, r = map(int, input().split())
o1 = o2 = 0
for _ in range(n):
    s = int(input())
    if s < r:
        o1 += 1
    elif s > r:
        o2 += 1

print(int(o1 != o2) + int(o1 < o2))
