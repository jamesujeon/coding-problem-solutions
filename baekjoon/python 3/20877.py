# 문제 링크: https://www.acmicpc.net/problem/20877

input()
print(sum(min(n, 7) - 2 - (i % 2) for i, n in enumerate(map(int, input().split()))))
