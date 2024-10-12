# 문제 링크: https://www.acmicpc.net/problem/13410

N, K = map(int, input().split())
print(max(int(str(N * i)[::-1]) for i in range(1, K + 1)))
