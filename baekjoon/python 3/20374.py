# 문제 링크: https://www.acmicpc.net/problem/20374

import sys
input = sys.stdin.readline

m = 0
while True:
    try:
        e, c = map(int, input().split('.'))
        m += e * 100 + c
    except:
        break

print(f"{m // 100}.{m % 100:02d}")
