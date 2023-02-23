# 문제 링크: https://www.acmicpc.net/problem/16479

K = int(input())
D1, D2 = map(int, input().split())

print(K**2 - ((D1 - D2) / 2)**2)
