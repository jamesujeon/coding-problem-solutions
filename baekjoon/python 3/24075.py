# 문제 링크: https://www.acmicpc.net/problem/24075

A, B = map(int, input().split())

print(max(A + B, A - B))
print(min(A + B, A - B))
