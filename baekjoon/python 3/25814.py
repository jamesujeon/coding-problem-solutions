# 문제 링크: https://www.acmicpc.net/problem/25814

a, b = map(lambda x: len(x) * sum(map(int, x)), input().split())

print(int(a != b) + int(a < b))
