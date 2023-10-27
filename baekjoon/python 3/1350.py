# 문제 링크: https://www.acmicpc.net/problem/1350

input()
f = map(int, input().split())
c = int(input())

print(-sum(-i // c for i in f if i > 0) * c)
