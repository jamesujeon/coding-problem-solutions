# 문제 링크: https://www.acmicpc.net/problem/24603

n, x, y = map(int, input().split())
for _ in range(n):
    print(int(int(input()) / x * y))
