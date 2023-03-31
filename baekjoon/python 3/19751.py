# 문제 링크: https://www.acmicpc.net/problem/19751

a, b, c, d = sorted(map(int, input().split()))

b, c = c, b

print(a, b, c, d)
