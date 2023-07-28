# 문제 링크: https://www.acmicpc.net/problem/25841

a, b, d = map(int, input().split())

d = str(d)
print(sum(str(i).count(d) for i in range(a, b + 1)))
