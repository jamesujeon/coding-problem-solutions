# 문제 링크: https://www.acmicpc.net/problem/24333

l1, r1, l2, r2, k = map(int, input().split())

print(sum(i != k for i in range(max(l1, l2), min(r1, r2) + 1)))
