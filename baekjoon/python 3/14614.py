# 문제 링크: https://www.acmicpc.net/problem/14614

A, B, C = map(int, input().split())
print(A ^ (C % 2 * B))
