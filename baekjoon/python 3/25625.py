# 문제 링크: https://www.acmicpc.net/problem/25625

x, y = map(int, input().split())

print(x + y if x > y else y - x)
