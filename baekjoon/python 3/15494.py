# 문제 링크: https://www.acmicpc.net/problem/15494

n = int(input()) // 364
for x in range(100, 0, -1):
    if n > x and (k := (n - x) / 3) % 1 == 0:
        print(x)
        print(int(k))
        break
