# 문제 링크: https://www.acmicpc.net/problem/5032

e, f, c = map(int, input().split())
print(max((e + f - 1) // (c - 1), 0))
