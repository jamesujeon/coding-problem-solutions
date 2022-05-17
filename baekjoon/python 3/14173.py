# 문제 링크: https://www.acmicpc.net/problem/14173

fx1, fy1, fx2, fy2 = map(int, input().split())
sx1, sy1, sx2, sy2 = map(int, input().split())

print(max(max(fx2, sx2) - min(fx1, sx1), max(fy2, sy2) - min(fy1, sy1)) ** 2)
