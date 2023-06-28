# 문제 링크: https://www.acmicpc.net/problem/24871

d, m, w = map(int, input().split())
i, j, k = map(int, input().split())

print(chr(97 + (d * m * (k - 1) + d * (j - 1) + i - 1) % w))
