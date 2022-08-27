# 문제 링크: https://www.acmicpc.net/problem/13118

points = list(map(int, input().split()))
x, _, _ = map(int, input().split())

print(points.index(x) + 1 if x in points else 0)
