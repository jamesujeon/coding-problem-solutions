# 문제 링크: https://www.acmicpc.net/problem/27294

T, S = map(int, input().split())
print(320 if 12 <= T <= 16 and S == 0 else 280)
