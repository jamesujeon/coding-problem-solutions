# 문제 링크: https://www.acmicpc.net/problem/24312

a, b, c, d = sorted(map(int, input().split()))

print(min(abs(a + d - b - c), abs(a + b + c - d)))
