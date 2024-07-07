# 문제 링크: https://www.acmicpc.net/problem/9883

x, y = map(int, input().split())
print(int(''.join(i + j for i, j in zip(bin(x)[2:].zfill(16), bin(y)[2:].zfill(16))), 2))
